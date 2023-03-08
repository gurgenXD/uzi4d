from django.contrib import admin
from django.http import HttpRequest

from app.models import Specialist, Specialization


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """Специализации в админ-панели."""

    list_display = ("guid", "name")

    def has_change_permission(self, _request: HttpRequest, _obj: Specialization|None =None) -> bool:
        """Права на изменение."""
        return False

    def has_add_permission(self, _request: HttpRequest) -> bool:
        """Права на добавление."""
        return False

    def has_delete_permission(self, _request: HttpRequest, _obj: Specialization|None=None) -> bool:
        """Права на удаление."""
        return False



@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    """Специалисты в админ-панели."""

    list_display = ("surname", "name", "patronymic", "on_main", "is_active")

    def has_change_permission(self, _request: HttpRequest, _obj: Specialist|None =None) -> bool:
        """Права на изменение."""
        return False

    def has_add_permission(self, _request: HttpRequest) -> bool:
        """Права на добавление."""
        return False

    def has_delete_permission(self, _request: HttpRequest, _obj: Specialist|None=None) -> bool:
        """Права на удаление."""
        return False
