from .models import KeystoneData
from django.contrib.auth.models import User
from .serializers import KeystoneDataSerializer, UserSerializer
from restapi.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import response
from rest_framework import schemas
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse


generator = schemas.SchemaGenerator(title='Keystone API')

@api_view()
@renderer_classes([renderers.CoreJSONRenderer])
def schema_view(request):
    schema = generator.get_schema(request)
    return response.Response(schema)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'keystonedata': reverse('keyst-list', request=request, format=format)
    })


class KeystoneCreateView(generics.ListCreateAPIView):
    queryset = KeystoneData.objects.all()
    serializer_class = KeystoneDataSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KeystoneDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = KeystoneData.objects.all()
    serializer_class = KeystoneDataSerializer
    lookup_field = 'field_name'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer