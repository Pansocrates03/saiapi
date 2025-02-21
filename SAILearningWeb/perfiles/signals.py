from .models import Perfil
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def post_save_create_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)