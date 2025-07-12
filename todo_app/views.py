from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect

from .forms import TaskForm
from .models import  Task,status_choices

def task_list(request):
    tasks = Task.objects.all()
    return  render(request,'task_list.html', context={'tasks':tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            extra_info = form.cleaned_data.get('extra_info')
            status = form.cleaned_data.get('status')
            finish_date = form.cleaned_data.get('finish_date')
            task = Task.objects.create(title=title,description=description, extra_info=extra_info ,status=status,finish_date=finish_date)
            return redirect('task_detail',pk = task.pk)
        else:
            return render(request,'add_task.html',{'form':form})
    else:
        form = TaskForm()
        return render(request, 'add_task.html',{'form':form})


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
        form = TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.extra_info = form.cleaned_data.get('extra_info')
            task.status = form.cleaned_data.get('status')
            task.finish_date = form.cleaned_data.get('finish_date')
            task.save()
            return redirect('task_detail',pk = task.pk)
        else:
            return  redirect('update_task',{'form':form})
    else:
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'extra_info': task.extra_info,
            'status': task.status,
            'finish_date': task.finish_date,
        })
        return  render(request,'task_update.html',{'form':form})