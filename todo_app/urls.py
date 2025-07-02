from django.urls import path,include
from todo_app.views import task_list

urlpatterns = [
    path('',task_list)
]
