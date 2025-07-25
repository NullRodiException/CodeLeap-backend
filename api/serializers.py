from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content']

    def get_username(self, obj):
        author = obj.author
        return author.first_name or author.username
