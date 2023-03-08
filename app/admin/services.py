from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from app.models import Service


@admin.register(Service)
class ServiceAdmin(DjangoMpttAdmin):
    """Услуги в админ-панели."""

    list_display = ("guid", "name", "is_group", "is_active", "on_main")

    def has_change_permission(self, _request, _obj=None):
        """Права на изменение."""
        return False

    def has_add_permission(self, _request):
        """Права на добавление."""
        return False

    def has_delete_permission(self, _request, _obj=None):
        """Права на удаление."""
        return False
