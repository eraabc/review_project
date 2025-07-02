from django.urls import path,include
from todo_app.views import task_list,add_task,task_detail,delete_task

urlpatterns = [
    path('',task_list),
    path('add-task/',add_task),
    path('task/',task_detail),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
]
