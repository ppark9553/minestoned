from rest_framework import (
    generics,
    permissions
)
from .serializers import KeystoneDataSerializer
from .models import KeystoneData


class KeystoneCreateView(generics.ListCreateAPIView):
    queryset = KeystoneData.objects.all()
    serializer_class = KeystoneDataSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class KeystoneDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = KeystoneData.objects.all()
    serializer_class = KeystoneDataSerializer