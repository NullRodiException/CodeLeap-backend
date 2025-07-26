from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'username', 'content', 'created_datetime']

    def get_username(self, obj):
        author = obj.author
        return author.first_name or author.username

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime',
                  'title', 'content', 'comments', 'likes_count']

    def get_username(self, obj):
        author = obj.author
        return author.first_name or author.username

    def get_likes_count(self, obj):
        return obj.likes.count()
