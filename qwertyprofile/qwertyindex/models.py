from django.db import models

# Create your models here.
class qwertyindex(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    github_url = models.CharField(max_length=200)
    github_project_url = models.CharField(max_length=300)
    description = models.TextField()
    image = models.FilePathField(path="/img")