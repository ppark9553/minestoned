from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class KeystoneData(models.Model):
    field = models.CharField(max_length=100, blank=False, unique=True)
    data = models.TextField()
    owner = models.ForeignKey('auth.User',
                              related_name='keystonedata')
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.field)

# This receiver handles token creation when a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)