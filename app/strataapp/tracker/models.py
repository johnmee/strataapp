from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Building(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Organisation(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    url = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Engagement(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT, related_name="engagements")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="engagements")
    service = models.CharField(max_length=200)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.organisation.name} — {self.service} @ {self.building.name}"


class Parcel(models.Model):
    AREA_TYPE_CHOICES = [
        ("private", "Private"),
        ("common", "Common"),
        ("exclusive", "Exclusive Use"),
    ]
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="parcels")
    name = models.CharField(max_length=200)
    area_type = models.CharField(max_length=20, choices=AREA_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_area_type_display()})"


class Tag(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="tags")
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        unique_together = [("building", "slug")]

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    organisation = models.ForeignKey(
        Organisation, null=True, blank=True, on_delete=models.SET_NULL, related_name="contacts"
    )
    hidden = models.BooleanField(default=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="contact"
    )

    def __str__(self):
        return self.display_name()

    def display_name(self):
        if self.name:
            return self.name
        if self.organisation_id:
            return f"{self.organisation.name} (office)"
        return "Unknown"

    def clean(self):
        if not self.name and not self.organisation_id:
            raise ValidationError("Contact must have a name or be linked to an organisation.")


class Tenure(models.Model):
    ROLE_CHOICES = [
        ("owner", "Owner"),
        ("tenant", "Tenant"),
    ]
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="tenures")
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE, related_name="tenures")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

    @property
    def is_current(self):
        return self.to_date is None

    def __str__(self):
        return f"{self.contact.display_name()} · {self.get_role_display()} · {self.parcel.name}"


class Issue(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="issues")
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="issues")
    parcels = models.ManyToManyField(Parcel, blank=True, related_name="issues")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def urgency_state(self):
        if self.completed_at is not None:
            return "done"
        if not self.pk:
            return "idle"
        now = timezone.now()
        try:
            active_events = self.events.filter(cancelled=False)
        except AttributeError:
            return "idle"
        if active_events.filter(date__gt=now).exists():
            return "waiting"
        if active_events.filter(date__lte=now).exists():
            return "active"
        return "idle"
