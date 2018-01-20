from .models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact 
        fields = ('__all__')

    def create(self, validated_data):
        """
        Create and return a new `Contact` instance, given the validated data.
        """
        return Contact.objects.create(**validated_data)
