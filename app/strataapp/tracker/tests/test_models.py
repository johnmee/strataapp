import pytest


@pytest.mark.django_db
def test_tracker_app_installed():
    from django.apps import apps
    assert apps.is_installed("tracker")
