from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
