from rest_framework import serializers
from ..models import Post
from .comment_serializer import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    name = serializers.ReadOnlyField(source='author.first_name')
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'name', 'username', 'created_datetime',
                  'title', 'content', 'comments', 'likes_count']

    def get_username(self, obj):
        if hasattr(obj.author, 'profile') and obj.author.profile.app_username:
            return obj.author.profile.app_username
        return obj.author.username

    def get_likes_count(self, obj):
        return obj.likes.count()
