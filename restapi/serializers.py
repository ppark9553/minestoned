from rest_framework import serializers
from .models import KeystoneData
from django.contrib.auth.models import User


class KeystoneDataSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = KeystoneData
        fields = ('id', 'url', 'field_name', 'field_data', 'owner', 'updated')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    keystonedata = serializers.HyperlinkedRelatedField(
        many=True, view_name='keyst-detail', read_only=True)

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'url', 'username', 'keystonedata')