from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    STATUS = (
        ('pending', 'pending'),
        ('done', 'done'),
        ('delayed', 'delayed'),
    )
    active_status = models.CharField(max_length=20,choices=STATUS, default='pending')

    def __str__(self):
        return self.title