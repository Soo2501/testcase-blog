from django.db import models
from django.contrib.auth.models import User
# Create your models here.file:///home/suraj/Documents/demo/animal/tests/test_models.py


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title