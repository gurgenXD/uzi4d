from django.contrib import admin

from app.models import Promotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    """Акции в админ-панели."""

    list_display = ("name", "sale", "date_start", "date_end", "on_main")
