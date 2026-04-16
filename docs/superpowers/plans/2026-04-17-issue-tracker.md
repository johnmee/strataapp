# Issue Tracker Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Django app for tracking strata maintenance issues and events against the data model in `docs/superpowers/specs/2026-04-16-issue-tracker-design.md`. Phase 1 is Django admin for data entry plus two read-only public pages (issue list, issue detail).

**Architecture:** A single new Django app, `tracker`, containing all ten models (Building, Organisation, Engagement, Contact, Parcel, Tenure, Tag, Issue, Event, Document). Computed states (Issue urgency, Event derived state) are model properties. Public views are plain Django class-based views with simple HTML templates. Tests use pytest-django with `@pytest.mark.django_db`.

**Tech Stack:**
- Python 3.14, Django 6.0.4 (already present)
- SQLite (development), FileField on disk for documents
- pytest 9.0.3 + pytest-django (new dev dependency)
- Plain Django templates (no CSS framework in phase 1)
- Package manager: `uv`

**Working directory:** all shell commands run from `/home/john/code/strataapp/app/strataapp/` unless stated otherwise.

**File structure:**
```
app/strataapp/tracker/                          ← new Django app
├── __init__.py
├── apps.py                                     ← AppConfig
├── admin.py                                    ← all admin registrations
├── models.py                                   ← all ten models
├── views.py                                    ← public read-only views
├── urls.py                                     ← /issues/ routes
├── migrations/
│   └── __init__.py
├── templates/tracker/
│   ├── base.html                               ← minimal layout shared by public pages
│   ├── issue_list.html
│   └── issue_detail.html
└── tests/
    ├── __init__.py
    ├── conftest.py                             ← fixtures (building, organisation, contact, etc.)
    ├── test_models.py                          ← model validation + computed properties
    ├── test_admin.py                           ← smoke tests for admin
    └── test_views.py                           ← public view rendering + hidden-contact redaction

app/pyproject.toml                              ← add pytest-django to dev group
app/strataapp/pytest.ini                        ← pytest-django configuration
app/strataapp/strataapp/settings.py             ← add tracker app, MEDIA settings
app/strataapp/strataapp/urls.py                 ← include tracker.urls
```

---

## Task 1: Dev dependencies and test harness

**Files:**
- Modify: `app/pyproject.toml`
- Create: `app/strataapp/pytest.ini`
- Create: `app/strataapp/tracker/__init__.py`
- Create: `app/strataapp/tracker/apps.py`
- Create: `app/strataapp/tracker/models.py`
- Create: `app/strataapp/tracker/migrations/__init__.py`
- Create: `app/strataapp/tracker/tests/__init__.py`
- Create: `app/strataapp/tracker/tests/test_models.py`
- Modify: `app/strataapp/strataapp/settings.py`

- [ ] **Step 1: Add pytest-django to dev dependencies**

Edit `app/pyproject.toml`, change the `[dependency-groups]` section to:

```toml
[dependency-groups]
dev = [
    "pytest>=9.0.3",
    "pytest-django>=4.9.0",
]
```

Then run:
```bash
cd /home/john/code/strataapp/app && uv sync
```

Expected: `pytest-django` installed into the project's virtual environment.

- [ ] **Step 2: Create pytest.ini**

Create `app/strataapp/pytest.ini` with:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = strataapp.settings
python_files = test_*.py
testpaths = tracker/tests
```

- [ ] **Step 3: Create the tracker app scaffold**

Create `app/strataapp/tracker/__init__.py` (empty).

Create `app/strataapp/tracker/apps.py`:

```python
from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracker"
```

Create `app/strataapp/tracker/models.py` (empty for now, we'll fill it in Task 2):

```python
# Models defined in subsequent tasks.
```

Create `app/strataapp/tracker/migrations/__init__.py` (empty).

Create `app/strataapp/tracker/tests/__init__.py` (empty).

- [ ] **Step 4: Register the app and add MEDIA settings**

Edit `app/strataapp/strataapp/settings.py`.

Change the INSTALLED_APPS block to:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home",
    "tracker",
]
```

At the bottom of the file, add:

```python
# Media files (uploaded documents)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

- [ ] **Step 5: Write a smoke test**

Create `app/strataapp/tracker/tests/test_models.py`:

```python
import pytest


@pytest.mark.django_db
def test_tracker_app_installed():
    from django.apps import apps
    assert apps.is_installed("tracker")
```

- [ ] **Step 6: Run the smoke test**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 1 test passed.

- [ ] **Step 7: Commit**

```bash
cd /home/john/code/strataapp && git add app/pyproject.toml app/uv.lock app/strataapp/pytest.ini app/strataapp/tracker/ app/strataapp/strataapp/settings.py && git commit -m "Add tracker app scaffold with pytest-django harness."
```

---

## Task 2: Building, Organisation, Engagement models

**Files:**
- Modify: `app/strataapp/tracker/models.py`
- Create: `app/strataapp/tracker/tests/conftest.py`
- Modify: `app/strataapp/tracker/tests/test_models.py`

- [ ] **Step 1: Write failing tests**

Edit `app/strataapp/tracker/tests/test_models.py`, replace the file's contents with:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: tests fail with `ImportError` (models don't exist yet).

- [ ] **Step 3: Implement the three models**

Replace `app/strataapp/tracker/models.py` with:

```python
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
```

- [ ] **Step 4: Create and run migrations**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py makemigrations tracker
```

Expected: `Migrations for 'tracker': tracker/migrations/0001_initial.py` listing Building, Organisation, Engagement.

- [ ] **Step 5: Create shared fixtures**

Create `app/strataapp/tracker/tests/conftest.py`:

```python
import datetime

import pytest


@pytest.fixture
def building(db):
    from tracker.models import Building
    return Building.objects.create(name="Acacia Gardens", address="1 Test St", slug="acacia-gardens")


@pytest.fixture
def organisation(db):
    from tracker.models import Organisation
    return Organisation.objects.create(name="Acme Plumbing", phone="02 1234 5678", email="office@acme.test")


@pytest.fixture
def today():
    return datetime.date(2026, 4, 17)
```

- [ ] **Step 6: Run tests to verify they pass**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 5 tests passed.

- [ ] **Step 7: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Add Building, Organisation, Engagement models."
```

---

## Task 3: Parcel and Tag models

**Files:**
- Modify: `app/strataapp/tracker/models.py`
- Modify: `app/strataapp/tracker/tests/conftest.py`
- Modify: `app/strataapp/tracker/tests/test_models.py`

- [ ] **Step 1: Write failing tests**

Append to `app/strataapp/tracker/tests/test_models.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 3 new tests fail with ImportError for Parcel/Tag.

- [ ] **Step 3: Add Parcel and Tag models**

Append to `app/strataapp/tracker/models.py`:

```python
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
```

- [ ] **Step 4: Migrate**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py makemigrations tracker
```

- [ ] **Step 5: Add fixture for parcel**

Append to `app/strataapp/tracker/tests/conftest.py`:

```python
@pytest.fixture
def parcel(db, building):
    from tracker.models import Parcel
    return Parcel.objects.create(building=building, name="Lot 1", area_type="private")
```

- [ ] **Step 6: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 8 tests passed.

- [ ] **Step 7: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Add Parcel and Tag models."
```

---

## Task 4: Contact model with name-or-organisation validation

**Files:**
- Modify: `app/strataapp/tracker/models.py`
- Modify: `app/strataapp/tracker/tests/conftest.py`
- Modify: `app/strataapp/tracker/tests/test_models.py`

- [ ] **Step 1: Write failing tests**

Append to `app/strataapp/tracker/tests/test_models.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 5 new tests fail (Contact doesn't exist).

- [ ] **Step 3: Implement Contact**

Append to `app/strataapp/tracker/models.py`:

```python
from django.conf import settings
from django.core.exceptions import ValidationError


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
```

- [ ] **Step 4: Migrate**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py makemigrations tracker
```

- [ ] **Step 5: Add contact fixtures**

Append to `app/strataapp/tracker/tests/conftest.py`:

```python
@pytest.fixture
def contact(db):
    from tracker.models import Contact
    return Contact.objects.create(name="Jane Doe", email="jane@example.test")


@pytest.fixture
def org_office_contact(db, organisation):
    from tracker.models import Contact
    return Contact.objects.create(name="", organisation=organisation)
```

- [ ] **Step 6: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 13 tests passed.

- [ ] **Step 7: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Add Contact model with name-or-organisation validation."
```

---

## Task 5: Tenure model

**Files:**
- Modify: `app/strataapp/tracker/models.py`
- Modify: `app/strataapp/tracker/tests/test_models.py`

- [ ] **Step 1: Write failing tests**

Append to `app/strataapp/tracker/tests/test_models.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 2 new tests fail.

- [ ] **Step 3: Implement Tenure**

Append to `app/strataapp/tracker/models.py`:

```python
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
```

- [ ] **Step 4: Migrate**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py makemigrations tracker
```

- [ ] **Step 5: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 15 tests passed.

- [ ] **Step 6: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Add Tenure model linking Contact to Parcel over time."
```

---

## Task 6: Issue model with urgency_state

**Files:**
- Modify: `app/strataapp/tracker/models.py`
- Modify: `app/strataapp/tracker/tests/conftest.py`
- Modify: `app/strataapp/tracker/tests/test_models.py`

- [ ] **Step 1: Write failing tests**

Append to `app/strataapp/tracker/tests/test_models.py`:

```python
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
```

(Note: urgency states `overdue`, `waiting`, and `active` depend on Event — tested in Task 7 after Event exists.)

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 3 new tests fail.

- [ ] **Step 3: Implement Issue**

Append to `app/strataapp/tracker/models.py`:

```python
from django.utils import timezone


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
```

**Note on the spec's `overdue` state:** The spec lists `overdue` for "a planned event with a past date," but the Event model defines `planned` as `date > now` — which is mutually exclusive with "past date." No event can simultaneously be both planned and past, so `overdue` is unreachable without an additional flag distinguishing "planned but now past" from "occurred." For phase 1 we omit `overdue` from the returned states (done / waiting / active / idle are the four reachable states). If the distinction matters, revisit by adding an explicit `occurred_at` flag to Event.

- [ ] **Step 4: Migrate**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py makemigrations tracker
```

- [ ] **Step 5: Add issue fixture**

Append to `app/strataapp/tracker/tests/conftest.py`:

```python
@pytest.fixture
def issue(db, building):
    from tracker.models import Issue
    return Issue.objects.create(building=building, title="Fix roof leak")
```

- [ ] **Step 6: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 18 tests passed.

- [ ] **Step 7: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Add Issue model with urgency_state property."
```

---

## Task 7: Event model with derived_state

**Files:**
- Modify: `app/strataapp/tracker/models.py`
- Modify: `app/strataapp/tracker/tests/conftest.py`
- Modify: `app/strataapp/tracker/tests/test_models.py`

- [ ] **Step 1: Write failing tests**

Append to `app/strataapp/tracker/tests/test_models.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 8 new tests fail.

- [ ] **Step 3: Implement Event**

Append to `app/strataapp/tracker/models.py`:

```python
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
```

- [ ] **Step 4: Migrate**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py makemigrations tracker
```

- [ ] **Step 5: Add event fixture**

Append to `app/strataapp/tracker/tests/conftest.py`:

```python
@pytest.fixture
def event(db, building, contact):
    from django.utils import timezone
    from tracker.models import Event
    e = Event.objects.create(building=building, event_type="meeting", date=timezone.now())
    e.contacts.add(contact)
    return e
```

- [ ] **Step 6: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 26 tests passed.

- [ ] **Step 7: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Add Event model with derived_state and display_title."
```

---

## Task 8: Document model with mimetype / size auto-detection

**Files:**
- Modify: `app/strataapp/tracker/models.py`
- Modify: `app/strataapp/tracker/tests/test_models.py`

- [ ] **Step 1: Write failing test**

Append to `app/strataapp/tracker/tests/test_models.py`:

```python
@pytest.mark.django_db
def test_document_auto_detects_mimetype_and_size(building, contact):
    from django.core.files.uploadedfile import SimpleUploadedFile
    from django.utils import timezone
    from tracker.models import Document, Event
    e = Event.objects.create(building=building, event_type="email", date=timezone.now())
    e.contacts.add(contact)
    upload = SimpleUploadedFile("report.pdf", b"%PDF-1.4 fake content", content_type="application/pdf")
    d = Document.objects.create(event=e, title="Site report", file=upload)
    assert d.mimetype == "application/pdf"
    assert d.file_size == len(b"%PDF-1.4 fake content")
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 1 new test fails.

- [ ] **Step 3: Implement Document**

Append to `app/strataapp/tracker/models.py`:

```python
import mimetypes


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
```

- [ ] **Step 4: Migrate**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py makemigrations tracker
```

- [ ] **Step 5: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 27 tests passed.

- [ ] **Step 6: Cleanup uploaded test files**

```bash
cd /home/john/code/strataapp/app/strataapp && rm -rf media/documents
```

(pytest-django creates real files for FileField tests; we don't want them in the commit.)

- [ ] **Step 7: Add media/ to gitignore if not already**

Check `/home/john/code/strataapp/.gitignore`. If `media/` is not listed, append it:

```bash
cd /home/john/code/strataapp && echo "app/strataapp/media/" >> .gitignore
```

- [ ] **Step 8: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ .gitignore && git commit -m "Add Document model with mimetype and size auto-detection."
```

---

## Task 9: Admin — Building, Organisation, Engagement, Tag, Parcel

**Files:**
- Create: `app/strataapp/tracker/admin.py`
- Create: `app/strataapp/tracker/tests/test_admin.py`

- [ ] **Step 1: Write smoke tests**

Create `app/strataapp/tracker/tests/test_admin.py`:

```python
import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def admin_client(db, client):
    User = get_user_model()
    user = User.objects.create_superuser(username="admin", password="admin-pass", email="a@a.test")
    client.force_login(user)
    return client


@pytest.mark.django_db
@pytest.mark.parametrize("app_label,model", [
    ("tracker", "building"),
    ("tracker", "organisation"),
    ("tracker", "engagement"),
    ("tracker", "parcel"),
    ("tracker", "tag"),
])
def test_admin_changelist_loads(admin_client, app_label, model):
    response = admin_client.get(f"/admin/{app_label}/{model}/")
    assert response.status_code == 200
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 5 new tests fail (404 because admin not registered).

- [ ] **Step 3: Create admin.py**

Create `app/strataapp/tracker/admin.py`:

```python
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
```

- [ ] **Step 4: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 32 tests passed.

- [ ] **Step 5: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Register Building, Organisation, Engagement, Tag, Parcel in admin."
```

---

## Task 10: Admin — Contact with Tenure inline and multi-field search

**Files:**
- Modify: `app/strataapp/tracker/admin.py`
- Modify: `app/strataapp/tracker/tests/test_admin.py`

- [ ] **Step 1: Write failing tests**

Append to `app/strataapp/tracker/tests/test_admin.py`:

```python
@pytest.mark.django_db
def test_contact_admin_changelist_loads(admin_client):
    response = admin_client.get("/admin/tracker/contact/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_contact_admin_search_by_phone(admin_client, organisation):
    from tracker.models import Contact
    Contact.objects.create(name="Jane", phone="0412 345 678", organisation=organisation)
    response = admin_client.get("/admin/tracker/contact/?q=0412")
    assert response.status_code == 200
    assert b"Jane" in response.content


@pytest.mark.django_db
def test_contact_admin_search_by_organisation_name(admin_client, organisation):
    from tracker.models import Contact
    Contact.objects.create(name="Jane", organisation=organisation)
    response = admin_client.get("/admin/tracker/contact/?q=Acme")
    assert response.status_code == 200
    assert b"Jane" in response.content
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 3 new tests fail (Contact not registered).

- [ ] **Step 3: Add Contact admin with Tenure inline**

Append to `app/strataapp/tracker/admin.py`:

```python
from tracker.models import Contact, Tenure


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
```

- [ ] **Step 4: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 35 tests passed.

- [ ] **Step 5: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Add Contact admin with Tenure inline and phone/org search."
```

---

## Task 11: Admin — Issue with urgency filter and events panel

**Files:**
- Modify: `app/strataapp/tracker/admin.py`
- Modify: `app/strataapp/tracker/tests/test_admin.py`

- [ ] **Step 1: Write failing tests**

Append to `app/strataapp/tracker/tests/test_admin.py`:

```python
@pytest.mark.django_db
def test_issue_admin_changelist_loads(admin_client):
    response = admin_client.get("/admin/tracker/issue/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_issue_admin_shows_urgency_column(admin_client, building):
    from tracker.models import Issue
    Issue.objects.create(building=building, title="Fix roof")
    response = admin_client.get("/admin/tracker/issue/")
    assert response.status_code == 200
    assert b"idle" in response.content  # urgency label appears


@pytest.mark.django_db
def test_issue_admin_filter_by_urgency_done(admin_client, building):
    from django.utils import timezone
    from tracker.models import Issue
    Issue.objects.create(building=building, title="Open item")
    Issue.objects.create(building=building, title="Closed item", completed_at=timezone.now())
    response = admin_client.get("/admin/tracker/issue/?urgency=done")
    assert response.status_code == 200
    assert b"Closed item" in response.content
    assert b"Open item" not in response.content
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 3 new tests fail.

- [ ] **Step 3: Add Issue admin with urgency filter**

Append to `app/strataapp/tracker/admin.py`:

```python
from tracker.models import Issue


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
        # urgency_state is a Python property; we filter in Python after fetching.
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
```

- [ ] **Step 4: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 38 tests passed.

- [ ] **Step 5: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Add Issue admin with urgency filter and event timeline."
```

---

## Task 12: Admin — Event with Document inline and derived state display

**Files:**
- Modify: `app/strataapp/tracker/admin.py`
- Modify: `app/strataapp/tracker/tests/test_admin.py`

- [ ] **Step 1: Write failing tests**

Append to `app/strataapp/tracker/tests/test_admin.py`:

```python
@pytest.mark.django_db
def test_event_admin_changelist_loads(admin_client):
    response = admin_client.get("/admin/tracker/event/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_event_admin_shows_derived_state(admin_client, event):
    response = admin_client.get("/admin/tracker/event/")
    assert response.status_code == 200
    assert b"occurred" in response.content or b"planned" in response.content


@pytest.mark.django_db
def test_event_admin_change_page_shows_derived_state_readonly(admin_client, event):
    response = admin_client.get(f"/admin/tracker/event/{event.pk}/change/")
    assert response.status_code == 200
    assert b"Derived state" in response.content or b"derived state" in response.content.lower()
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 3 new tests fail.

- [ ] **Step 3: Add Event admin with Document inline**

Append to `app/strataapp/tracker/admin.py`:

```python
from tracker.models import Document, Event


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
```

- [ ] **Step 4: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 41 tests passed.

- [ ] **Step 5: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ && git commit -m "Add Event admin with Document inline and derived state display."
```

---

## Task 13: Public issue list view

**Files:**
- Create: `app/strataapp/tracker/views.py`
- Create: `app/strataapp/tracker/urls.py`
- Modify: `app/strataapp/strataapp/urls.py`
- Create: `app/strataapp/tracker/templates/tracker/base.html`
- Create: `app/strataapp/tracker/templates/tracker/issue_list.html`
- Create: `app/strataapp/tracker/tests/test_views.py`

- [ ] **Step 1: Write failing tests**

Create `app/strataapp/tracker/tests/test_views.py`:

```python
import pytest
from django.utils import timezone


@pytest.mark.django_db
def test_issue_list_renders(client, building):
    from tracker.models import Issue
    Issue.objects.create(building=building, title="Fix lift")
    response = client.get("/issues/")
    assert response.status_code == 200
    assert b"Fix lift" in response.content


@pytest.mark.django_db
def test_issue_list_shows_urgency_badge(client, building):
    from tracker.models import Issue
    Issue.objects.create(building=building, title="Idle issue")
    Issue.objects.create(building=building, title="Done issue", completed_at=timezone.now())
    response = client.get("/issues/")
    assert response.status_code == 200
    assert b"idle" in response.content
    assert b"done" in response.content


@pytest.mark.django_db
def test_issue_list_no_auth_required(client, building):
    from tracker.models import Issue
    Issue.objects.create(building=building, title="Public issue")
    response = client.get("/issues/")
    assert response.status_code == 200
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 3 new tests fail with 404.

- [ ] **Step 3: Create the view**

Create `app/strataapp/tracker/views.py`:

```python
from django.views.generic import ListView

from tracker.models import Issue


class IssueListView(ListView):
    model = Issue
    template_name = "tracker/issue_list.html"
    context_object_name = "issues"

    def get_queryset(self):
        return Issue.objects.all().prefetch_related("tags", "parcels", "events")
```

- [ ] **Step 4: Create the URL config**

Create `app/strataapp/tracker/urls.py`:

```python
from django.urls import path

from tracker.views import IssueListView

app_name = "tracker"

urlpatterns = [
    path("issues/", IssueListView.as_view(), name="issue_list"),
]
```

Modify `app/strataapp/strataapp/urls.py` — change the urlpatterns list to:

```python
from django.contrib import admin
from django.urls import include, path
from home.views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("", include("tracker.urls")),
]
```

- [ ] **Step 5: Create the base template**

Create `app/strataapp/tracker/templates/tracker/base.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{% block title %}Strata Tracker{% endblock %}</title>
    <style>
        body { font-family: sans-serif; max-width: 960px; margin: 2em auto; padding: 0 1em; }
        table { border-collapse: collapse; width: 100%; }
        th, td { text-align: left; padding: 0.5em; border-bottom: 1px solid #ddd; }
        .badge { display: inline-block; padding: 0.1em 0.5em; border-radius: 0.25em; font-size: 0.85em; }
        .badge-done { background: #e0e0e0; color: #444; }
        .badge-overdue { background: #fee; color: #c00; }
        .badge-waiting { background: #eef; color: #339; }
        .badge-active { background: #efe; color: #060; }
        .badge-idle { background: #f5f5f5; color: #888; }
    </style>
</head>
<body>
    <h1><a href="/issues/">Strata Tracker</a></h1>
    {% block content %}{% endblock %}
</body>
</html>
```

- [ ] **Step 6: Create the issue list template**

Create `app/strataapp/tracker/templates/tracker/issue_list.html` with this exact content (the detail-page link is deferred to Task 14 because the URL doesn't exist yet and `{% url %}` would fail to reverse):

```html
{% extends "tracker/base.html" %}
{% block title %}Issues — Strata Tracker{% endblock %}
{% block content %}
<h2>Issues</h2>
{% if issues %}
<table>
    <thead>
        <tr>
            <th>Title</th>
            <th>State</th>
            <th>Tags</th>
            <th>Last activity</th>
        </tr>
    </thead>
    <tbody>
        {% for issue in issues %}
        <tr>
            <td>{{ issue.title }}</td>
            <td><span class="badge badge-{{ issue.urgency_state }}">{{ issue.urgency_state }}</span></td>
            <td>{% for tag in issue.tags.all %}{{ tag.name }}{% if not forloop.last %}, {% endif %}{% endfor %}</td>
            <td>{% with last=issue.events.all|dictsort:"date"|last %}{% if last %}{{ last.date|date:"Y-m-d" }}{% endif %}{% endwith %}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% else %}
<p>No issues yet.</p>
{% endif %}
{% endblock %}
```

- [ ] **Step 7: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 44 tests passed.

- [ ] **Step 8: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ app/strataapp/strataapp/urls.py && git commit -m "Add public issue list view and template."
```

---

## Task 14: Public issue detail view

**Files:**
- Modify: `app/strataapp/tracker/views.py`
- Modify: `app/strataapp/tracker/urls.py`
- Modify: `app/strataapp/tracker/templates/tracker/issue_list.html`
- Create: `app/strataapp/tracker/templates/tracker/issue_detail.html`
- Modify: `app/strataapp/tracker/tests/test_views.py`

- [ ] **Step 1: Write failing tests**

Append to `app/strataapp/tracker/tests/test_views.py`:

```python
@pytest.mark.django_db
def test_issue_detail_renders(client, building, contact):
    from tracker.models import Event, Issue
    i = Issue.objects.create(building=building, title="Fix roof leak")
    e = Event.objects.create(building=building, event_type="meeting", date=timezone.now())
    e.contacts.add(contact)
    e.issues.add(i)
    response = client.get(f"/issues/{i.pk}/")
    assert response.status_code == 200
    assert b"Fix roof leak" in response.content
    assert b"Meeting" in response.content
    assert b"Jane Doe" in response.content


@pytest.mark.django_db
def test_issue_detail_redacts_hidden_contacts(client, building):
    from tracker.models import Contact, Event, Issue
    hidden = Contact.objects.create(name="Secret Person", hidden=True)
    i = Issue.objects.create(building=building, title="Legal matter")
    e = Event.objects.create(building=building, event_type="email", date=timezone.now())
    e.contacts.add(hidden)
    e.issues.add(i)
    response = client.get(f"/issues/{i.pk}/")
    assert response.status_code == 200
    assert b"Secret Person" not in response.content


@pytest.mark.django_db
def test_issue_detail_shows_documents(client, building, contact):
    from django.core.files.uploadedfile import SimpleUploadedFile
    from tracker.models import Document, Event, Issue
    i = Issue.objects.create(building=building, title="Report")
    e = Event.objects.create(building=building, event_type="email", date=timezone.now())
    e.contacts.add(contact)
    e.issues.add(i)
    Document.objects.create(
        event=e,
        title="Engineer report",
        file=SimpleUploadedFile("report.pdf", b"fake", content_type="application/pdf"),
    )
    response = client.get(f"/issues/{i.pk}/")
    assert response.status_code == 200
    assert b"Engineer report" in response.content


@pytest.mark.django_db
def test_issue_list_links_to_detail(client, building):
    from tracker.models import Issue
    i = Issue.objects.create(building=building, title="Link test")
    response = client.get("/issues/")
    assert response.status_code == 200
    assert f"/issues/{i.pk}/".encode() in response.content
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 4 new tests fail.

- [ ] **Step 3: Add the detail view**

Modify `app/strataapp/tracker/views.py` to read:

```python
from django.views.generic import DetailView, ListView

from tracker.models import Issue


class IssueListView(ListView):
    model = Issue
    template_name = "tracker/issue_list.html"
    context_object_name = "issues"

    def get_queryset(self):
        return Issue.objects.all().prefetch_related("tags", "parcels", "events")


class IssueDetailView(DetailView):
    model = Issue
    template_name = "tracker/issue_detail.html"
    context_object_name = "issue"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["events"] = self.object.events.order_by("-date").prefetch_related(
            "contacts", "parcels", "documents"
        )
        return ctx
```

- [ ] **Step 4: Add the URL**

Modify `app/strataapp/tracker/urls.py` to read:

```python
from django.urls import path

from tracker.views import IssueDetailView, IssueListView

app_name = "tracker"

urlpatterns = [
    path("issues/", IssueListView.as_view(), name="issue_list"),
    path("issues/<int:pk>/", IssueDetailView.as_view(), name="issue_detail"),
]
```

- [ ] **Step 5: Restore the link in the list template**

In `app/strataapp/tracker/templates/tracker/issue_list.html`, change the title cell back to:

```html
            <td><a href="{% url 'tracker:issue_detail' issue.pk %}">{{ issue.title }}</a></td>
```

- [ ] **Step 6: Create the detail template**

Create `app/strataapp/tracker/templates/tracker/issue_detail.html`:

```html
{% extends "tracker/base.html" %}
{% block title %}{{ issue.title }} — Strata Tracker{% endblock %}
{% block content %}
<p><a href="{% url 'tracker:issue_list' %}">&larr; All issues</a></p>

<h2>{{ issue.title }}</h2>
<p><span class="badge badge-{{ issue.urgency_state }}">{{ issue.urgency_state }}</span></p>

{% if issue.description %}<p>{{ issue.description|linebreaks }}</p>{% endif %}

{% if issue.tags.all %}
<p><strong>Tags:</strong>
{% for tag in issue.tags.all %}{{ tag.name }}{% if not forloop.last %}, {% endif %}{% endfor %}
</p>
{% endif %}

{% if issue.parcels.all %}
<p><strong>Parcels:</strong>
{% for p in issue.parcels.all %}{{ p.name }}{% if not forloop.last %}, {% endif %}{% endfor %}
</p>
{% endif %}

<h3>Event timeline</h3>
{% if events %}
<ul>
{% for e in events %}
<li>
    <strong>{{ e.date|date:"Y-m-d H:i" }}</strong> ·
    <span class="badge badge-{{ e.derived_state }}">{{ e.derived_state }}</span> ·
    {{ e.get_event_type_display }}
    {% if e.duration %} ({{ e.duration }}){% endif %}
    <br>
    <em>
    {% for c in e.contacts.all %}{% if not c.hidden %}{{ c.display_name }}{% else %}(hidden){% endif %}{% if not forloop.last %}, {% endif %}{% endfor %}
    </em>
    {% if e.description %}<br>{{ e.description|linebreaks }}{% endif %}
    {% if e.parcels.all %}
    <br><small>Parcels: {% for p in e.parcels.all %}{{ p.name }}{% if not forloop.last %}, {% endif %}{% endfor %}</small>
    {% endif %}
    {% if e.documents.all %}
    <br><small>Documents:
    {% for d in e.documents.all %}<a href="{{ d.file.url }}">{{ d.title }}</a>{% if not forloop.last %}, {% endif %}{% endfor %}
    </small>
    {% endif %}
    {% if e.rescheduled_to.all %}
    <br><small>Rescheduled to event #{{ e.rescheduled_to.first.pk }}</small>
    {% endif %}
</li>
{% endfor %}
</ul>
{% else %}
<p>No events logged for this issue yet.</p>
{% endif %}
{% endblock %}
```

- [ ] **Step 7: Add MEDIA URL routing for DEBUG mode**

Modify `app/strataapp/strataapp/urls.py` to serve uploaded files in development. Replace the file's contents with:

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from home.views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("", include("tracker.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- [ ] **Step 8: Run tests**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: 48 tests passed.

- [ ] **Step 9: Cleanup any uploaded test files**

```bash
cd /home/john/code/strataapp/app/strataapp && rm -rf media/documents
```

- [ ] **Step 10: Commit**

```bash
cd /home/john/code/strataapp && git add app/strataapp/tracker/ app/strataapp/strataapp/urls.py && git commit -m "Add public issue detail view with event timeline and hidden-contact redaction."
```

---

## Task 15: Apply migrations and create initial Building

**Files:**
- (no code changes — one-off setup)

- [ ] **Step 1: Apply all migrations to the dev database**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py migrate
```

Expected: all tracker migrations applied to `db.sqlite3`.

- [ ] **Step 2: Create a superuser (interactive)**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py createsuperuser
```

Follow prompts. Username, email, password — user's choice.

- [ ] **Step 3: Start the dev server to smoke test**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run python manage.py runserver
```

In a browser:
- Visit `http://127.0.0.1:8000/admin/` — log in, confirm the Tracker section appears with all ten models.
- Create a Building record.
- Create an Organisation, an Issue, and an Event with at least one Contact.
- Visit `http://127.0.0.1:8000/issues/` — the issue should appear.
- Click through to the detail view — the event should appear.

Stop the server with Ctrl-C when done.

- [ ] **Step 4: Run the full test suite one more time**

```bash
cd /home/john/code/strataapp/app/strataapp && uv run pytest -v
```

Expected: all 48 tests pass.

- [ ] **Step 5: Nothing to commit for this task**

This task is verification-only; db.sqlite3 changes are local and gitignored.

---

## Self-Review

**1. Spec coverage:**

| Spec requirement | Task |
|---|---|
| Building model | 2 |
| Organisation model with phone/email/url | 2 |
| Engagement model | 2 |
| Contact model with optional name, validation, user OneToOne | 4 |
| Parcel model | 3 |
| Tenure model | 5 |
| Tag model | 3 |
| Issue model with urgency_state | 6 (plus events-dependent states verified in 7) |
| Event model with derived_state, display_title, rescheduled_from | 7 |
| Document model with mimetype/size auto-detect | 8 |
| Admin: Building, Tag, Parcel, Organisation (no inline Engagement) | 9 |
| Admin: Contact with Tenure inline, phone search | 10 |
| Admin: Issue with urgency filter, linked events panel | 11 |
| Admin: Event with Document inline, derived state label | 12 |
| Public Issue list | 13 |
| Public Issue detail with hidden-contact redaction | 14 |
| Multi-tenancy preserved (building FK on models that need it) | 2–7 |

**2. Placeholders:** None. Every step contains full code or exact commands.

**3. Type consistency:** related_name conventions are consistent (`parcels`, `events`, `engagements`, `contacts`, `issues`, `tags`, `tenures`, `documents`, `rescheduled_to`). Property names match across templates and admin (`urgency_state`, `derived_state`, `display_title`, `display_name`, `is_current`).

**4. Known limitation documented:** the `overdue` urgency state is unreachable given the current data model (no flag distinguishes "was planned, should have occurred, didn't" from "occurred"). Task 6 notes this explicitly for the implementer. The other four states (`done`, `waiting`, `active`, `idle`) are fully reachable and tested.

**5. Out-of-scope deferrals confirmed:** no signal for auto-creating Contact on User creation (spec says "created at account setup" — treated as manual admin step for phase 1). No per-building queryset filtering in Event admin widgets (not needed for single-building deployment; spec flags multi-tenancy as a future phase). No rich text (user dropped the requirement).
