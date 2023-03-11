from django.db import models


class Rating(models.Model):
    """Рейтинг."""

    name = models.CharField("Источник", max_length=30)
    score = models.CharField("Рейтинг", max_length=3)
    reviews_count = models.TextField("Количество отзывов", blank=True)
    photo = models.FileField("Фото")
    link = models.URLField("Ссылка", max_length=255)

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def __str__(self):
        return self.name
