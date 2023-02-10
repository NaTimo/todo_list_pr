from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.views.generic import TemplateView

from .models import Task

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ["text"]
    success_url = "/todo_list_app/tasklist/"
    template_name = "user_task_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    fields = ["text"]
    success_url = "/todo_list_app/tasklist/"
    template_name = "user_task_form.html"

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    success_url = "/todo_list_app/tasklist/"
    template_name = "task_delete.html"
    context_object_name = "task"

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user