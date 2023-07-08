from django.shortcuts import render,get_object_or_404,redirect
from .forms import TaskForm
from .models import Task

def task_list(request):
    if request.user.is_superuser:
        tasks=Task.objects.all()
    else:
        tasks=Task.objects.filter(assigned_to=request.user)

    print(tasks)
    
    return render(request,'todolist/task_list.html',{'tasks':tasks})

def task_detail(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    return render(request,'todolist/task_detail.html',{'task':task})

def update_task_status(request,task_id):
    task=get_object_or_404(Task,id=task_id)

    if request.method=='POST':
        #updating the task
        status=request.POST.get('status')
        task.status=status
        task.save()

    return render(request,'todolist/update_task_status.html',{'task':task})