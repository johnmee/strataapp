from django.db import models


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
