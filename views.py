from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

def home(request):
    todo_items = Todo.objects.all().order_by('-added_date') 
    context = {
        'todo_items':todo_items
    }
    return render(request, 'todo/index.html', context)

#get data from home or user
def add_todo(request): 
    #print(request.POST)
    current_date = timezone.now()
    content = request.POST['content']

    created_object = Todo.objects.create(added_date=current_date, text=content)
    print(created_object)
    # print(added_date)
    # print(content)
    # length_of_todos = Todo.objects.all().count()
    # print(length_of_todos)

    return redirect('/')

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')