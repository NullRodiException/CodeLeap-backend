from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    mentions = models.ManyToManyField(User, related_name='mentioned_in_posts', blank=True)

    def __str__(self):
        return self.title