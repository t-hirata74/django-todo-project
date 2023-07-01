from django.urls import path
from . import views
from .views import TaskCreate, TaskList, TaskDetail, TaskUpdate

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(),
         name="task"),  # <int:pk>は動的パス, pkはプライマリーキー
    path("create-task/", TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task"),
]
