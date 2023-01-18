from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
