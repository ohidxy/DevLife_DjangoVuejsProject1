from .models import Contact
from rest_framework import serializers
from django.contrib.auth.models import User

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact 
        fields = ('__all__')