from django.shortcuts import render, redirect, get_object_or_404
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm

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


# Update view
def todo_list_update(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todolist)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=todolist)

    context = {
        "todolist": todolist,
        "form": form,
    }
    return render(request, "todos/edit.html", context)


# Delete view
def todo_list_delete(request, id):
    todolist = TodoList.objects.get(id=id)
    if request.method == "POST":
        todolist.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")


# Create TodoItem view
def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()
    context = {
        "form": form,
    }
    return render(request, "todos/items/create.html", context)


# Update TodoItem
def todo_item_update(request, id):
    # item = TodoItem.objects.get(id=id)
    item = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm(instance=item)
    context = {
        "form": form,
    }
    return render(request, "todos/items/edit.html", context)
