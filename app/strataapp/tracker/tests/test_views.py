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
