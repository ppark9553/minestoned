from django.contrib import admin
from .models import KeystoneData

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)

# Register your models here.
admin.site.register(KeystoneData)
