from django.db import models

# Create your models here.

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Framework', 'Framework'),
        ('Langage', 'Langage'),
        ('DevOps', 'DevOps'),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Langage')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=300, blank=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    category = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"