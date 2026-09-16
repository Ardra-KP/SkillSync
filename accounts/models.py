from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, default='developer')
    
    
    title = models.CharField(max_length=100, blank=True, help_text="Eg: Full Stack Developer")
    skills = models.CharField(max_length=500, blank=True, help_text="Eg: Python, Django, React")
    bio = models.TextField(blank=True)
    
    
    location = models.CharField(max_length=100, blank=True, default="Kochi, Kerala")
    hourly_rate = models.IntegerField(default=500, help_text="Rate per hour in INR")
    experience = models.IntegerField(default=0, help_text="Years of experience")
    
    github = models.URLField(blank=True, verbose_name="GitHub URL")
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn URL")
    portfolio = models.URLField(blank=True, verbose_name="Portfolio Website")
    
    availability = models.BooleanField(default=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.CharField(max_length=100, help_text="Eg: ₹5000 - ₹10000")
    skills_required = models.CharField(max_length=500, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Open', choices=STATUS_CHOICES)
    
    
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='proposals')
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    bid_amount = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.developer.username} - {self.project.title}"