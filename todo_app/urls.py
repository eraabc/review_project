from django.urls import path
from todo_app.views import TaskListView,AddTaskView,DetailView,DeleteTaskView,UpdateTaskView

urlpatterns = [
    path('',TaskListView.as_view(),name='task_list'),
    path('add-task/',AddTaskView.as_view(),name='add_task'),
    path('task/<slug:slug>',DetailView.as_view(),name='task_detail'),
    path('tasks/delete/<int:task_id>/', DeleteTaskView.as_view(), name='delete_task'),
    path('task/<int:pk>/update/',UpdateTaskView.as_view(), name='update_task'),
]
