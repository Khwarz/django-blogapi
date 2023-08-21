from django.conf import settings
from django.db import models


class Post(models.Model):
    title: models.CharField = models.CharField(max_length=255)
    body: models.TextField = models.TextField()
    author: models.ForeignKey = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
