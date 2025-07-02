from django.shortcuts import render


def task_list(request):
    return  render(request,'task_list.html')