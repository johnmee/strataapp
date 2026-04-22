from django.contrib import admin

from tracker.models import Building, Engagement, Organisation, Parcel, Tag


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "address")


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    search_fields = ("name", "phone", "email")


@admin.register(Engagement)
class EngagementAdmin(admin.ModelAdmin):
    list_display = ("organisation", "building", "service", "from_date", "to_date")
    list_filter = ("building", "service")
    search_fields = ("organisation__name", "service")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "building", "slug")
    list_filter = ("building",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ("name", "building", "area_type")
    list_filter = ("building", "area_type")
    search_fields = ("name",)
