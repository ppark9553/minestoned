from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    KeystoneCreateView,
    KeystoneDetailsView
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',
                            namespace='rest_framework')),
    url(r'^keyst/create/$', KeystoneCreateView.as_view(), name="keyst_create"),
    url(r'^keyst/(?P<field>[\w.@+-]+)/$',
            KeystoneDetailsView.as_view(), name="keyst_details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)