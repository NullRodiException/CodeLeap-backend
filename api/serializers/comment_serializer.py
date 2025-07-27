from rest_framework import serializers
from ..models import Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    name = serializers.ReadOnlyField(source='author.first_name')

    class Meta:
        model = Comment
        fields = ['id', 'name', 'username', 'content', 'created_datetime']

    def get_username(self, obj):
        author = obj.author
        if hasattr(author, 'profile') and author.profile.app_username:
            return author.profile.app_username
        return author.username
