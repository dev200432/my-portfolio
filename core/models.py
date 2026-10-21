from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(default=80)

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"