from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks, 'form':form}
    
    return render(request, 'todo/home.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    
    form = TaskForm(instance=task)

    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'form':form}
    return render(request, 'todo/update_task.html', context)

def delete(request, pk):

    # item = Task.objects.get(id=pk)
    # item.delete()

    # return redirect('/')


    item = Task.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
        

    return render(request, 'todo/delete.html', context)