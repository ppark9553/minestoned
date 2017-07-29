from rest_framework import serializers
from .models import KeystoneData
from django.contrib.auth.models import User


class KeystoneDataSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = KeystoneData
        fields = ('field', 'data', 'owner', 'time_updated')
        read_only_fields = ('time_updated')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    keystonedata = serializers.PrimaryKeyRelatedField(
        many=True, queryset=KeystoneData.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'keystonedata')