from django.urls import path,include
from todo_app.views import task_list,add_task,task_detail

urlpatterns = [
    path('',task_list),
    path('add-task/',add_task),
    path('task/',task_detail)
]
