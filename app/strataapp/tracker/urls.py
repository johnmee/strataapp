from django.urls import path

from tracker.views import IssueListView

app_name = "tracker"

urlpatterns = [
    path("issues/", IssueListView.as_view(), name="issue_list"),
]
