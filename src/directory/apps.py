from django.apps import AppConfig


class DirectoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.directory'
    verbose_name = "Directory"

    def ready(self):
        import src.directory.signals
