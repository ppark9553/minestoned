from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import KeystoneDataSerializer, UserSerializer
from .models import KeystoneData
from django.contrib.auth.models import User


class KeystoneCreateView(generics.ListCreateAPIView):
    queryset = KeystoneData.objects.all()
    serializer_class = KeystoneDataSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KeystoneDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = KeystoneData.objects.all()
    serializer_class = KeystoneDataSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer