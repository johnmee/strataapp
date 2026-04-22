import mimetypes

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
        active_events = self.events.filter(cancelled=False)
        if active_events.filter(date__gt=now).exists():
            return "waiting"
        if active_events.filter(date__lte=now).exists():
            return "active"
        return "idle"


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ("phone_call", "Phone Call"),
        ("email", "Email"),
        ("meeting", "Meeting"),
        ("conversation", "Conversation"),
        ("notice", "Notice"),
        ("work", "Work"),
        ("observation", "Observation"),
        ("other", "Other"),
    ]
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    cancelled = models.BooleanField(default=False)
    date = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)
    rescheduled_from = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rescheduled_to",
    )
    issues = models.ManyToManyField(Issue, blank=True, related_name="events")
    contacts = models.ManyToManyField(Contact, blank=True, related_name="events")
    parcels = models.ManyToManyField(Parcel, blank=True, related_name="events")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.display_title

    @property
    def derived_state(self):
        if self.pk and self.rescheduled_to.exists():
            return "rescheduled"
        if self.cancelled:
            return "cancelled"
        if self.date > timezone.now():
            return "planned"
        return "occurred"

    @property
    def display_title(self):
        if self.title:
            return self.title
        primary = self.contacts.first() if self.pk else None
        contact_name = primary.display_name() if primary else "Unknown"
        return f"{self.get_event_type_display()} · {contact_name} · {self.date.strftime('%d %b %Y')}"


class Document(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="documents")
    file = models.FileField(upload_to="documents/%Y/%m/")
    title = models.CharField(max_length=300)
    mimetype = models.CharField(max_length=100, blank=True)
    file_size = models.PositiveIntegerField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.file and not self.mimetype:
            guessed, _ = mimetypes.guess_type(self.file.name)
            if guessed:
                self.mimetype = guessed
        if self.file and self.file_size is None:
            try:
                self.file_size = self.file.size
            except (OSError, ValueError):
                self.file_size = None
        super().save(*args, **kwargs)
