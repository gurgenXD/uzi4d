from enum import Enum

from django.db import models


class UpdaterStatusType(Enum):
    """Статусы обновления."""

    PROCESSING = "processing"
    SUCCESS = "success"
    FAILURE = "failure"


class Updater(models.Model):
    """Обновления."""

    start_update = models.DateTimeField("Время начала")
    end_update = models.DateTimeField("Время окончания", null=True, blank=True)
    status = models.CharField("Статус", max_length=20)
    error_log = models.TextField("Текст ошибки", blank=True)

    class Meta:
        verbose_name = "Обновление"
        verbose_name_plural = "Обновления"

    def __str__(self):
        return f"{self.id} - {self.status}"
