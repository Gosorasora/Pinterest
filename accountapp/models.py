from django.db import models

# Create your models here.

class helloWorld(models.Model):
    text = models.TextField(max_length=500, null = False)
