import re

from rest_framework import serializers
from ..models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    name = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'app_username']
        read_only_fields = ['name', 'email']

    def validate_app_username(self, value):
        if not re.match(r'^[\w]+$', value):
            raise serializers.ValidationError(
                'O nome de usuário pode conter apenas letras, números e underscores (_).'
            )
        return value
