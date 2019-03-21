from django.conf import settings
from django.db.models.signals import post_save 
from django.core.mail import send_mail
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        
        send_mail(
            '가입환영이메일',
            'Travel 블로그에 가입을 환영합니다!',
            'nldaseul@gmail.com',
            ['to@gmail.com'],
            fail_silently=False,
        )

post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)
