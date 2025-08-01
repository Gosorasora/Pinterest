from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    #로그인을 확인할려면 필요하지 않나 ? 외래키 ?
    # project_user = models.ForeignKey(User,on_delete=models.SET_NULL, related_name='project', null=True)

    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)

