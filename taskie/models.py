from django.db import models

# Create your models here.


class ToDoList(models.Model):
    # type of field
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    # define saying we are using a forign key from todolist imput
    ToDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
