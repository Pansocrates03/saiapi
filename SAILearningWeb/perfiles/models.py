from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email').blank = False

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nivel = models.IntegerField(default=1)
    #imagen = models.ImageField(upload_to='perfiles/', default='perfiles/default.jpg')

    def __str__(self):
        return self.usuario.username
    
    class Meta:
        verbose_name_plural = "Perfiles"