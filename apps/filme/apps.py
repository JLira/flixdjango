from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.filme'

    def ready(self):
        import apps.filme.signals
