from rest_framework import serializers
from app_main.models import Note
from django.contrib.auth import models

User = models

class NoteSerializer(serializers.ModelSerializer):
   class Meta:
      model = Note
      fields = ['id','owner', 'title','body', 'created','updated']


class UserSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = ['fist_name','last_name','username', 'email','password']