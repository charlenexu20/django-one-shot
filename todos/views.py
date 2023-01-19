from django.shortcuts import render, redirect
from todos.models import TodoList
from todos.forms import TodoListForm

# Create your views here.


# Show all todolists
def todo_list_list(request):
    todolists = TodoList.objects.all()
    context = {
        "todolists": todolists,
    }
    return render(request, "todos/list.html", context)


# Show detail of one of the todolists
def todo_list_detail(request, id):
    todolist = TodoList.objects.get(id=id)
    context = {
        "todolist": todolist,
    }
    return render(request, "todos/detail.html", context)


# Create view
def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todolist = form.save()
            return redirect("todo_list_detail", id=todolist.id)
    else:
        form = TodoListForm()

    context = {
        "form": form,
    }

    return render(request, "todos/create.html", context)
