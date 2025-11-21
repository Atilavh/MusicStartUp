from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.account_app'
    label = 'account_app'

    def ready(self):
        from apps.account_app.signals import signals
