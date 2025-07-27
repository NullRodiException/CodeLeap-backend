import re

from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Post
from .comment_serializer import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    name = serializers.ReadOnlyField(source='author.first_name')
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    mentions = serializers.SlugRelatedField(many=True, read_only=True, slug_field='profile__app_username')

    class Meta:
        model = Post
        fields = ['id', 'name', 'username', 'created_datetime', 'title', 'content', 'comments', 'likes_count', 'mentions']

    def get_username(self, obj):
        if hasattr(obj.author, 'profile') and obj.author.profile.app_username:
            return obj.author.profile.app_username
        return obj.author.username

    def get_likes_count(self, obj):
        return obj.likes.count()

    def update_mentions(self, instance, content):
        usernames = re.findall(r'@(\w+)', content)
        if not usernames:
            instance.mentions.clear()
            return

        mentioned_users = User.objects.filter(profile__app_username__in=usernames)
        instance.mentions.set(mentioned_users)

    def create(self, validated_data):
        post = super().create(validated_data)
        self.update_mentions(post, validated_data.get('content', ''))
        return post

    def update(self, instance, validated_data):
        post = super().update(instance, validated_data)
        if 'content' in validated_data:
            self.update_mentions(post, validated_data['content'])
        return post

