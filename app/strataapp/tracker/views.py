from django.views.generic import ListView

from tracker.models import Issue


class IssueListView(ListView):
    model = Issue
    template_name = "tracker/issue_list.html"
    context_object_name = "issues"

    def get_queryset(self):
        return Issue.objects.all().prefetch_related("tags", "parcels", "events")
