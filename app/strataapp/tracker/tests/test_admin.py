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
