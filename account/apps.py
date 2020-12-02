from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'

    def ready():
        from .signals import create_user_portfolio
