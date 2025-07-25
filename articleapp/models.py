from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # 회원 탈퇴 시 알 수 없음 on_delete

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    # 자동으로 생성시간 추가
    created_at = models.DateTimeField(auto_now_add=True, null=True)
