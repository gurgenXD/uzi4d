from django.db import models


class Promotion(models.Model):
    """Акции."""

    name = models.CharField("Название", max_length=100)
    sale = models.CharField("Скидка", max_length=100)
    description = models.TextField("Описание", blank=True)
    photo = models.ImageField("Фото")
    date_start = models.DateField("Начало акции")
    date_end = models.DateField("Конец акции")
    on_main = models.BooleanField("Выводить на главной")

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.name
