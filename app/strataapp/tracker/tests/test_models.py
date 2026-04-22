import datetime
import pytest


@pytest.mark.django_db
def test_tracker_app_installed():
    from django.apps import apps
    assert apps.is_installed("tracker")


@pytest.mark.django_db
def test_building_str_returns_name():
    from tracker.models import Building
    b = Building.objects.create(name="Acacia Gardens", address="1 Test St", slug="acacia-gardens")
    assert str(b) == "Acacia Gardens"


@pytest.mark.django_db
def test_building_slug_must_be_unique():
    from django.db import IntegrityError
    from tracker.models import Building
    Building.objects.create(name="A", address="a", slug="dup")
    with pytest.raises(IntegrityError):
        Building.objects.create(name="B", address="b", slug="dup")


@pytest.mark.django_db
def test_organisation_str_returns_name():
    from tracker.models import Organisation
    o = Organisation.objects.create(name="Acme Plumbing")
    assert str(o) == "Acme Plumbing"


@pytest.mark.django_db
def test_engagement_has_nullable_to_date():
    from tracker.models import Building, Engagement, Organisation
    o = Organisation.objects.create(name="Acme Strata")
    b = Building.objects.create(name="A", address="a", slug="a")
    e = Engagement.objects.create(
        organisation=o,
        building=b,
        service="Strata Manager",
        from_date=datetime.date(2024, 1, 1),
    )
    assert e.to_date is None


@pytest.mark.django_db
def test_parcel_str_includes_area_type(building):
    from tracker.models import Parcel
    p = Parcel.objects.create(building=building, name="Lot 5", area_type="private")
    assert "Lot 5" in str(p)


@pytest.mark.django_db
def test_parcel_area_type_choices(building):
    from tracker.models import Parcel
    p = Parcel.objects.create(building=building, name="Roof", area_type="common")
    assert p.get_area_type_display() == "Common"


@pytest.mark.django_db
def test_tag_str_returns_name(building):
    from tracker.models import Tag
    t = Tag.objects.create(building=building, name="Plumbing", slug="plumbing")
    assert str(t) == "Plumbing"


@pytest.mark.django_db
def test_contact_display_name_returns_name_when_present():
    from tracker.models import Contact
    c = Contact(name="Jane Doe")
    assert c.display_name() == "Jane Doe"


@pytest.mark.django_db
def test_contact_display_name_falls_back_to_org_office(organisation):
    from tracker.models import Contact
    c = Contact(name="", organisation=organisation)
    assert c.display_name() == "Acme Plumbing (office)"


@pytest.mark.django_db
def test_contact_validation_requires_name_or_organisation():
    from django.core.exceptions import ValidationError
    from tracker.models import Contact
    c = Contact(name="", organisation=None)
    with pytest.raises(ValidationError):
        c.full_clean()


@pytest.mark.django_db
def test_contact_validation_allows_name_only():
    from tracker.models import Contact
    c = Contact(name="Jane Doe")
    c.full_clean()  # no exception


@pytest.mark.django_db
def test_contact_validation_allows_org_only(organisation):
    from tracker.models import Contact
    c = Contact(organisation=organisation)
    c.full_clean()  # no exception


@pytest.mark.django_db
def test_tenure_current_when_to_date_null(contact, parcel):
    from tracker.models import Tenure
    t = Tenure.objects.create(
        contact=contact,
        parcel=parcel,
        role="owner",
        from_date=datetime.date(2020, 1, 1),
    )
    assert t.to_date is None
    assert t.is_current is True


@pytest.mark.django_db
def test_tenure_not_current_when_to_date_set(contact, parcel):
    from tracker.models import Tenure
    t = Tenure.objects.create(
        contact=contact,
        parcel=parcel,
        role="tenant",
        from_date=datetime.date(2020, 1, 1),
        to_date=datetime.date(2022, 1, 1),
    )
    assert t.is_current is False


@pytest.mark.django_db
def test_issue_urgency_done_when_completed(building):
    from django.utils import timezone
    from tracker.models import Issue
    i = Issue.objects.create(building=building, title="Fix roof", completed_at=timezone.now())
    assert i.urgency_state == "done"


@pytest.mark.django_db
def test_issue_urgency_idle_when_no_events(building):
    from tracker.models import Issue
    i = Issue.objects.create(building=building, title="Paint lobby")
    assert i.urgency_state == "idle"


@pytest.mark.django_db
def test_issue_str_returns_title(building):
    from tracker.models import Issue
    i = Issue.objects.create(building=building, title="Fix lift")
    assert str(i) == "Fix lift"


@pytest.mark.django_db
def test_event_state_planned_when_future(building, contact):
    from django.utils import timezone
    from tracker.models import Event
    future = timezone.now() + datetime.timedelta(days=3)
    e = Event.objects.create(building=building, event_type="meeting", date=future)
    e.contacts.add(contact)
    assert e.derived_state == "planned"


@pytest.mark.django_db
def test_event_state_occurred_when_past(building, contact):
    from django.utils import timezone
    from tracker.models import Event
    past = timezone.now() - datetime.timedelta(days=3)
    e = Event.objects.create(building=building, event_type="meeting", date=past)
    e.contacts.add(contact)
    assert e.derived_state == "occurred"


@pytest.mark.django_db
def test_event_state_cancelled(building, contact):
    from django.utils import timezone
    from tracker.models import Event
    e = Event.objects.create(
        building=building, event_type="meeting", date=timezone.now(), cancelled=True
    )
    e.contacts.add(contact)
    assert e.derived_state == "cancelled"


@pytest.mark.django_db
def test_event_state_rescheduled_when_another_event_points_to_it(building, contact):
    from django.utils import timezone
    from tracker.models import Event
    old = Event.objects.create(building=building, event_type="meeting", date=timezone.now())
    old.contacts.add(contact)
    new = Event.objects.create(
        building=building,
        event_type="meeting",
        date=timezone.now() + datetime.timedelta(days=7),
        rescheduled_from=old,
    )
    new.contacts.add(contact)
    assert old.derived_state == "rescheduled"


@pytest.mark.django_db
def test_event_display_title_auto_generated(building, contact):
    from django.utils import timezone
    from tracker.models import Event
    e = Event.objects.create(
        building=building,
        event_type="phone_call",
        date=timezone.datetime(2026, 4, 17, 10, 0, tzinfo=datetime.timezone.utc),
    )
    e.contacts.add(contact)
    t = e.display_title
    assert "Phone Call" in t
    assert "Jane Doe" in t
    assert "2026" in t


@pytest.mark.django_db
def test_event_display_title_uses_explicit_title_when_set(building, contact):
    from django.utils import timezone
    from tracker.models import Event
    e = Event.objects.create(
        building=building,
        event_type="meeting",
        title="AGM Q1 2026",
        date=timezone.now(),
    )
    e.contacts.add(contact)
    assert e.display_title == "AGM Q1 2026"


@pytest.mark.django_db
def test_issue_urgency_waiting_with_future_planned_event(building, contact, issue):
    from django.utils import timezone
    from tracker.models import Event
    future = timezone.now() + datetime.timedelta(days=3)
    e = Event.objects.create(building=building, event_type="meeting", date=future)
    e.contacts.add(contact)
    e.issues.add(issue)
    assert issue.urgency_state == "waiting"


@pytest.mark.django_db
def test_issue_urgency_active_with_recent_occurred_event(building, contact, issue):
    from django.utils import timezone
    from tracker.models import Event
    past = timezone.now() - datetime.timedelta(days=3)
    e = Event.objects.create(building=building, event_type="meeting", date=past)
    e.contacts.add(contact)
    e.issues.add(issue)
    assert issue.urgency_state == "active"
