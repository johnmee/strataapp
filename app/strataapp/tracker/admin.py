from django.contrib import admin

from tracker.models import Building, Contact, Document, Engagement, Event, Issue, Organisation, Parcel, Tag, Tenure


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


class TenureInline(admin.TabularInline):
    model = Tenure
    extra = 0
    fields = ("parcel", "role", "from_date", "to_date")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("display_name", "email", "phone", "organisation", "hidden")
    list_filter = ("hidden", "organisation")
    search_fields = ("name", "phone", "email", "organisation__name")
    inlines = [TenureInline]


class UrgencyStateListFilter(admin.SimpleListFilter):
    title = "urgency"
    parameter_name = "urgency"

    def lookups(self, request, model_admin):
        return [
            ("done", "Done"),
            ("overdue", "Overdue"),
            ("waiting", "Waiting"),
            ("active", "Active"),
            ("idle", "Idle"),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if not value:
            return queryset
        ids = [i.pk for i in queryset if i.urgency_state == value]
        return queryset.filter(pk__in=ids)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "building", "urgency_state", "completed_at", "created_at")
    list_filter = (UrgencyStateListFilter, "building", "tags")
    search_fields = ("title", "description")
    filter_horizontal = ("tags", "parcels")
    readonly_fields = ("created_at", "urgency_state", "linked_events_html")
    fieldsets = (
        (None, {"fields": ("building", "title", "description")}),
        ("Classification", {"fields": ("tags", "parcels")}),
        ("Status", {"fields": ("completed_at", "urgency_state", "created_at")}),
        ("Events", {"fields": ("linked_events_html",)}),
    )

    def linked_events_html(self, obj):
        from django.utils.html import format_html, format_html_join
        if not obj.pk:
            return "—"
        events = obj.events.order_by("-date")
        if not events.exists():
            return "No events linked yet."
        rows = format_html_join(
            "",
            "<li>{} · <strong>{}</strong> · {}</li>",
            (
                (e.date.strftime("%Y-%m-%d %H:%M"), e.derived_state, e.display_title)
                for e in events
            ),
        )
        return format_html("<ul>{}</ul>", rows)

    linked_events_html.short_description = "Event timeline"


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 0
    fields = ("title", "file", "mimetype", "file_size", "uploaded_at")
    readonly_fields = ("mimetype", "file_size", "uploaded_at")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("display_title", "building", "event_type", "date", "derived_state")
    list_filter = ("building", "event_type", "cancelled")
    search_fields = ("title", "description")
    filter_horizontal = ("issues", "contacts", "parcels")
    readonly_fields = ("created_at", "derived_state")
    fieldsets = (
        (None, {"fields": ("building", "title", "event_type", "date", "duration", "description")}),
        ("State", {"fields": ("cancelled", "rescheduled_from", "derived_state")}),
        ("Links", {"fields": ("issues", "contacts", "parcels")}),
        ("Meta", {"fields": ("created_at",)}),
    )
    inlines = [DocumentInline]
