from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import  Task,status_choices

def task_list(request):
    tasks = Task.objects.all()
    return  render(request,'task_list.html', context={'tasks':tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        extra_info = request.POST.get('extra_info')
        status = request.POST.get('status')
        finish_date = request.POST.get('finish_date')
        task = Task.objects.create(title=title,description=description, extra_info=extra_info ,status=status,finish_date=finish_date)
        return redirect('task_detail',pk = task.pk)
    else:
        return render(request, 'add_task.html',{'status_choices':status_choices})


def task_detail(request,**kwargs):
    task_id = kwargs.get('pk')
    task = get_object_or_404(Task,pk=task_id)
    return render(request,'task_detail.html',{'task':task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return HttpResponseRedirect(f'/task_detail/?id={task_id}')

def update_task(request,*args , pk , **kwargs):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.extra_info = request.POST.get('extra_info')
        task.status = request.POST.get('status')
        task.finish_date = request.POST.get('finish_date')
        task.save()
        return redirect('task_detail',pk = task.pk)
    else:
        return  render(request,'task_update.html',{'task':task,'status_choices':status_choices})