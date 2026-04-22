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
