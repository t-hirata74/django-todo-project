from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView

from todoapp.models import Task

# def taskList(request):
#     return HttpResponse("<h1>Hello Django</h1>")


class TaskList(ListView):
    model = Task
    context_object_name = "tasks"


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"  # modelsのtaskのfieldを一括で宣言できる
    # urlsのtasksにルートされる, クラスベースビューの際はリバースレイジー(更新後にtasksにリダイレクト)
    success_url = reverse_lazy("tasks")


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"  # modelsのtaskのfieldを一括で宣言できる
    # urlsのtasksにルートされる, クラスベースビューの際はリバースレイジー(更新後にtasksにリダイレクト)
    success_url = reverse_lazy("tasks")


class TaskDelete(DeleteView):
    model = Task
    fields = "__all__"  # modelsのtaskのfieldを一括で宣言できる
    # urlsのtasksにルートされる, クラスベースビューの際はリバースレイジー(更新後にtasksにリダイレクト)
    success_url = reverse_lazy("tasks")
    context_object_name = "task"


class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name = "todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")
