from django.db import models

# Create your models here.
class qwertyindex(models.Model):
    name = models.CharField(max_length=100)
    github_url = models.CharField(max_length=200)
    github_project_url = models.CharField(max_length=300)

class Subscibemodel(models.Model):

    email = models.EmailField()
    class Meta:
        verbose_name = ('email')
        verbose_name_plural = ('email')
