from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.conf import settings
from .models import Usuario
import os

@receiver(post_migrate)
def criar_superusuario(sender, **kwargs):
    if sender.name == 'apps.filme':
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")
        
        if email and senha:
            usuarios = Usuario.objects.filter(email=email)
            if not usuarios:
                Usuario.objects.create_superuser(
                    username="admin", email=email, password=senha, is_active=True, is_staff=True
                )
