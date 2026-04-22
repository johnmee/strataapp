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
