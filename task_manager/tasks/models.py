from django.db import models
from users.models import User
from .const import TaskState,PriorityState
from projects.models import Project


# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name=models.CharField(max_length=150)
    owner=models.ForeignKey(User,related_name="tasks",on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    description=models.TextField()
    state=models.CharField(max_length=100,choices=TaskState.choices,default=TaskState.todo)
    priority = models.CharField(max_length=100, choices=PriorityState.choices, default=PriorityState.low)
    due_date = models.DateField(null=True, blank=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tasks")
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content=models.TextField()
    owner = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username

