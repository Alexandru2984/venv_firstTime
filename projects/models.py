from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    github_link = models.URLField()
    link_text = models.CharField(max_length=255, default='Vezi Proiectul')

    def __str__(self):
        return self.title
    
class GitHubRepo(models.Model):
    name = models.CharField(max_length=255)
    html_url = models.URLField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name