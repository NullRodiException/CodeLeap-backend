import re
from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    name = serializers.ReadOnlyField(source='author.first_name')
    mentions = serializers.SlugRelatedField(many=True, read_only=True, slug_field='profile__app_username')

    class Meta:
        model = Comment
        fields = ['id', 'name', 'username', 'content', 'created_datetime', 'mentions']

    def get_username(self, obj):
        author = obj.author
        if hasattr(author, 'profile') and author.profile.app_username:
            return author.profile.app_username
        return author.username

    def update_mentions(self, instance, content):
        usernames = re.findall(r'@(\w+)', content)
        if not usernames:
            instance.mentions.clear()
            return
        mentioned_users = User.objects.filter(profile__app_username__in=usernames)
        instance.mentions.set(mentioned_users)

    def create(self, validated_data):
        comment = super().create(validated_data)
        self.update_mentions(comment, validated_data.get('content', ''))
        return comment

    def update(self, instance, validated_data):
        comment = super().update(instance, validated_data)
        if 'content' in validated_data:
            self.update_mentions(comment, validated_data['content'])
        return comment
