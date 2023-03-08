from django.contrib import admin
from app.models import Specialist, SpecialistCertificate, Specialization


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("guid", "name")

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ("surname", "name", "patronymic", "on_main", "is_active")

    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
