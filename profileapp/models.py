from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    # 객체가 없어지면 모델은 CASCADE해라.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profileapp/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.TextField(null=True)

