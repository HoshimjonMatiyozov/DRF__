from rest_framework import serializers
from django.contrib.auth import get_user_model

from app_main.models import Note

User = get_user_model()

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'body', 'created', 'updated']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username', 'email', 'password']
