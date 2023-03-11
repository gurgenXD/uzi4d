from django.contrib import admin

from app.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинги в админ-панели."""

    list_display = ("name", "score", "reviews_count")
