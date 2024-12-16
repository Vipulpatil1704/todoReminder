from django.urls import path
from .views import TaskListCreateView, TaskDetailView, DeleteAllTasksView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/delete-all/', DeleteAllTasksView.as_view(), name='delete-all-tasks'),
    path('tasks/<str:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/delete/<str:pk>/', TaskDetailView.as_view(), name='delete-task'),
]
