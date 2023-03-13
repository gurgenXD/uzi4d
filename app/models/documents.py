from django.db import models


class DocumentCategory(models.Model):
    """Категория документов."""

    name = models.CharField("Название", max_length=30)

    class Meta:
        verbose_name = "Категория документа"
        verbose_name_plural = "Категории документов"

    def __str__(self):
        return self.name


class Document(models.Model):
    """Документ."""

    name = models.CharField("Название", max_length=30)
    file = models.FileField("Документ")
    link = models.URLField("Ссылка", max_length=255, blank=True)

    category = models.ForeignKey(
        "DocumentCategory",
        on_delete=models.CASCADE,
        related_name="documents",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.name


class License(models.Model):
    """Лицензия."""

    name = models.CharField("Название", max_length=30)
    number = models.CharField("Номер", max_length=50)
    file = models.FileField("Документ")
    link = models.URLField("Ссылка", max_length=255, blank=True)

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"

    def __str__(self):
        return self.name
