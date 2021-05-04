from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoList

# Create your views here.
def home(request):
    todo_list = ToDo.objects
    form = ToDoList
    return render(request, 'todo_list.html', {'todo_list':todo_list, 'form':form})

def create(request):
    if request.method == 'POST':
        form = ToDoList(request.POST)
        if form.is_valid():
            todo = form.save(commit=True)
            todo.save()
    return redirect('home')
        

def update(request, id):
    if request.method == 'POST':
        update_todo = ToDo.objects.get(id=id)
        update_todo.todo = request.POST['todo']
        update_todo.save()
        return redirect('home')
    else:
        todo = ToDo.objects.get(id=id)
        return render(request, 'todo_item.html', {'todo':todo})

def delete(request, id):
    delete_todo = ToDo.objects.get(id=id)
    delete_todo.delete()
    return redirect('home') 
