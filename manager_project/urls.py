from django.contrib import admin
from django.urls import path

from manager import views as manager_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("worker_list/", manager_view.WorkerListView.as_view()),
]
