from .models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('__all__')