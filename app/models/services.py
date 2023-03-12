import mptt
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Service(models.Model):
    """Услуги."""

    guid = models.CharField("GUID", max_length=36, primary_key=True)
    name = models.CharField("Название", max_length=255)
    short_description = models.CharField("Короткое описание", max_length=255, blank=True)
    description = models.TextField("Описание", blank=True)
    preparation = models.TextField("Подготовка", blank=True)

    categories = models.ManyToManyField(
        "ServiceCategory", related_name="services", verbose_name="Категории", blank=True
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class ServiceCategory(MPTTModel):
    """Категория услуг."""

    guid = models.CharField("GUID", max_length=36, primary_key=True)
    name = models.CharField("Название", max_length=255)

    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="children",
        verbose_name="GUID родителя",
        blank=True,
        null=True,
    )

    catalog = models.ForeignKey(
        "ServiceCatalog",
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Каталог",
    )

    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"

    def __str__(self):
        return self.name


mptt.register(ServiceCategory)


class ServiceCatalog(models.Model):
    """Каталог услуг."""

    guid = models.CharField("GUID", max_length=36, primary_key=True)
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Каталог услуг"
        verbose_name_plural = "Каталоги услуг"

    def __str__(self):
        return self.name
