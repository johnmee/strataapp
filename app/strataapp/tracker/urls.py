from django.urls import path

from tracker.views import IssueDetailView, IssueListView

app_name = "tracker"

urlpatterns = [
    path("issues/", IssueListView.as_view(), name="issue_list"),
    path("issues/<int:pk>/", IssueDetailView.as_view(), name="issue_detail"),
]
