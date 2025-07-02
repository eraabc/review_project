from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import  Task,status_choices

def task_list(request):
    tasks = Task.objects.all()
    return  render(request,'task_list.html', context={'tasks':tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        finish_date = request.POST.get('finish_date')
        Task.objects.create(title=title,description=description,status=status,finish_date=finish_date)
        return  HttpResponseRedirect('/')
    else:
        return render(request, 'add_task.html',{'status_choices':status_choices})


def task_detail(request):
    task_id = request.GET.get('id')
    if task_id:
        try:
            task = Task.objects.get(id=task_id)
            return render(request,'task_detail.html',{'task':task})
        except Task.DoesNotExist:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect('/')
    return HttpResponseRedirect(f'/task_detail/?id={task_id}')