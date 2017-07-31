from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings


class KeystoneData(models.Model):
    field_name = models.CharField(max_length=100, blank=False, unique=True)
    field_data = models.TextField()
    owner = models.ForeignKey('auth.User',
                              related_name='keystonedata',
                              on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.field_name)

# This receiver handles token creation when a new user is created.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)