from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import TaskForm
from .models import  Task


class TaskListView(View):
    def get(self,request,*args,**kwargs):
        tasks = Task.objects.order_by('-created_at')
        return  render(request,'task_list.html', context={'tasks':tasks})


class AddTaskView(View):
    def post(self,request,*args,**kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail',slug = task.slug)
        else:
            return render(request,'add_task.html',{'form':form})

    def get(self,request,*args,**kwargs):
        form = TaskForm()
        return render(request, 'add_task.html', {'form': form})




class DetailView(TemplateView):
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.get(slug=self.kwargs['slug'])
        return context




class DeleteTaskView(View):
    def post(self,request,task_id,*args,**kwargs):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('task_list')

    def get(self,request,task_id,*args,**kwargs):
        task = get_object_or_404(Task, id=task_id)
        return render(request, 'confirm_delete.html', {'task': task})


class UpdateTaskView(View):
    def post(self,request,*args,pk,**kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', slug=task.slug)
        else:
            return render(request, 'task_update.html', {'form': form})

    def get(self,request,*args,pk,**kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'task_update.html', {'form': form})

