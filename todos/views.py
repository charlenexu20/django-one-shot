from django.shortcuts import render
from todos.models import TodoList

# Create your views here.


def todo_list_list(request):
    todolists = TodoList.objects.all()
    context = {
        "todolists": todolists,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todolist = TodoList.objects.get(id=id)
    context = {
        "todolist": todolist,
    }
    return render(request, "todos/detail.html", context)
