from django.db import models
from django.conf import settings

class Eassay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    body = models.TextField()

class Album(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    desc = models.CharField(max_length=100)

class Files(models.Model):
    # 변수명 무조건 author?
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False, upload_to="files")
    desc = models.CharField(max_length=100)
