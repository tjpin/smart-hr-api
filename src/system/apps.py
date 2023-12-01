from django.apps import AppConfig


class SystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.system'
    verbose_name = "System Manager"
    
    def ready(self) -> None:
        import src.system.signals
