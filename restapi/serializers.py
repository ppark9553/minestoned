from rest_framework import serializers
from .models import KeystoneData


class KeystoneDataSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = KeystoneData
        fields = ('owner', 'field', 'data', 'time_updated')
        read_only_fields = ('time_updated')