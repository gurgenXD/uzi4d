from django.contrib import admin
from django.http import HttpRequest
from django_mptt_admin.admin import DjangoMpttAdmin

from app.models import Service


@admin.register(Service)
class ServiceAdmin(DjangoMpttAdmin):
    """Услуги в админ-панели."""

    list_display = ("guid", "name", "is_group", "is_active", "on_main")

    def has_change_permission(self, _request: HttpRequest, _obj: Service|None =None) -> bool:
        """Права на изменение."""
        return False

    def has_add_permission(self, _request: HttpRequest) -> bool:
        """Права на добавление."""
        return False

    def has_delete_permission(self, _request: HttpRequest, _obj: Service|None=None) -> bool:
        """Права на удаление."""
        return False
