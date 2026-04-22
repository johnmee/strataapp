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


@pytest.fixture
def parcel(db, building):
    from tracker.models import Parcel
    return Parcel.objects.create(building=building, name="Lot 1", area_type="private")


@pytest.fixture
def contact(db):
    from tracker.models import Contact
    return Contact.objects.create(name="Jane Doe", email="jane@example.test")


@pytest.fixture
def org_office_contact(db, organisation):
    from tracker.models import Contact
    return Contact.objects.create(name="", organisation=organisation)
