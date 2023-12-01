from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.account'
    verbose_name = "Accounts and Staffs"

    def ready(self):
        import src.account.signals
