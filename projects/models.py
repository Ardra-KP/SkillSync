from django.db import models
from django.contrib.auth.models import User

class project(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget_min = models.IntegerField()
    budget_max = models.IntegerField()
    skills_needed = models.CharField(max_length=300)
    deadline_days = models.IntegerField(default=20)
    created_at =models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title
