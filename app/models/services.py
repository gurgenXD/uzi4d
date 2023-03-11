import mptt
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Service(MPTTModel):
    """Услуги."""

    guid = models.CharField("GUID", max_length=36, primary_key=True)
    name = models.CharField("Название", max_length=255)
    short_description = models.CharField("Короткое описание", max_length=255, null=True, blank=True)
    description = models.TextField("Короткое описание", null=True, blank=True)
    is_group = models.BooleanField("Группа")
    is_active = models.BooleanField("Активно")
    on_main = models.BooleanField("Показывать на главной")

    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="children",
        verbose_name="GUID родителя",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


mptt.register(Service)
