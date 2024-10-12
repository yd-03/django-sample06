from django.shortcuts import render
from django.views.generic import TemplateView

from manager.models import *


class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        workers = Worker.objects.all()
        context["workers"] = workers
        return render(request, self.template_name, context)
