from django.db import models
from django.contrib.auth.models import User
from api.models.post_model import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    mentions = models.ManyToManyField(User, related_name='mentioned_in_comments', blank=True)

    class Meta:
        ordering = ['created_datetime']

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'