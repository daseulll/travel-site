from django.conf import settings
from django.db.models.signals import post_save 
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']

post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)
