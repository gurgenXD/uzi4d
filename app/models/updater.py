from django.db import models

from enum import Enum


class UpdaterStatusType(Enum):
    """Статусы обновления."""

    PROCESSING = "processing"
    SUCCESS = "success"
    FAILURE = "failure"


class Updater(models.Model):
    """Обновления."""

    start_update = models.DateTimeField("Время налача")
    end_update = models.DateTimeField("Время окончания", null=True, blank=True)
    status = models.CharField("Статус", max_length=20)
    error_log = models.TextField("Текст ошибки", null=True, blank=True)

    class Meta:
        verbose_name = "Обновление"
        verbose_name_plural = "Обновления"

    def __str__(self) -> str:
        return f"{self.id} - {self.status}"
