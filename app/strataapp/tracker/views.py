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
