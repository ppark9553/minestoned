from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from .views import (
    api_root,
    KeystoneCreateView,
    KeystoneDetailsView,
    UserViewSet
)

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = {
    url(r'^$', api_root),
    url(r'^auth-token/', obtain_auth_token, name='auth-token'),
    url(r'^keyst/$', KeystoneCreateView.as_view(), name="keyst-list"),
    url(r'^keyst/(?P<field_name>[\w.@+-]+)/$', KeystoneDetailsView.as_view(), name="keyst-detail"),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
}

urlpatterns = format_suffix_patterns(urlpatterns)