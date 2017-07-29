from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    KeystoneCreateView,
    KeystoneDetailsView,
    UserView,
    UserDetailsView
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {

    url(r'^auth/', include('rest_framework.urls',namespace='rest_framework')),

    url(r'^token/', obtain_auth_token),

    url(r'^keyst/$', KeystoneCreateView.as_view(), name="keyst_create"),

    url(r'^keyst/(?P<field>[\w.@+-]+)/$', KeystoneDetailsView.as_view(), name="keyst_details"),

    url(r'^users/$', UserView.as_view(), name="users"),

    url(r'users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),

}

urlpatterns = format_suffix_patterns(urlpatterns)