from django.db import models

# Create your models here.
class file(models.Model):
    files = models.FileField(upload_to='media/images')