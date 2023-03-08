from django.contrib import admin

from app.models import City, Department, Office


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Города в админ-панели."""


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Отделения в админ-панели."""


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    """Филиалы в админ-панели."""
