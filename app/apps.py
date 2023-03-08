from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    """Настройки приложения."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
    verbose_name = "Приложения"
