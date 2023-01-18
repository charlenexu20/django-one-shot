from django.urls import path
from todos.views import todo_list_list, todo_list_detail


urlpatterns = [
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("", todo_list_list, name="todo_list_list"),
]
