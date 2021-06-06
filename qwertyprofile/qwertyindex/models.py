from django.db import models

# Create your models here.
class qwertyindex(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FilePathField(path="/img")