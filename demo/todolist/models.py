from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES=(
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    )

    title=models.CharField(max_length=100)
    description=models.TextField()
    due_date=models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, default=None)
    lead=models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_tasks')
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')

    def __str__(self):
        return self.title