from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("tasklist/", views.TaskListView.as_view(), name="task_list"),
    path("createtask/", views.TaskCreateView.as_view(), name="create_task"),
    path("tasklist/<int:pk>/update", views.TaskUpdateView.as_view(), name="update_task"),
    path("tasklist/<int:pk>/delete", views.TaskDeleteView.as_view(), name="delete_task"),
]