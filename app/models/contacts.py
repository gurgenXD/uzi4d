from django.db import models


class City(models.Model):
    """Город."""

    name = models.CharField("Название", max_length=30)
    is_active = models.BooleanField("Активно")

    def get_active_offices(self):
        """Получить активные филиалы."""
        return self.offices.filter(is_active=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Office(models.Model):
    """Филиалы."""

    description = models.CharField("Описание", max_length=100)
    address = models.CharField("Адрес", max_length=100)
    work_time = models.CharField("Рабочее время", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.CharField("E-mail", max_length=30)
    main_doctor = models.CharField("Главный врач", max_length=50)
    main_doctor_work_time = models.CharField("Приёмные часы", max_length=100)
    coor_x = models.CharField("Координата X", max_length=10)
    coor_y = models.CharField("Координата Y", max_length=10)
    is_active = models.BooleanField("Активно")

    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, related_name="offices", verbose_name="Город"
    )

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"

    def __str__(self):
        return self.address


class Department(models.Model):
    """Отделения."""

    name = models.CharField("Название", max_length=100)
    tags = models.CharField("Теги", max_length=100, blank=True)
    short_description = models.CharField("Короткое описание", max_length=300)
    description = models.TextField("Описание", max_length=300)
    photo = models.ImageField("Фотография")
    is_active = models.BooleanField("Активно")

    office = models.ForeignKey(
        "Office", on_delete=models.CASCADE, related_name="departaments", verbose_name="Филиал"
    )

    class Meta:
        verbose_name = "Отделение"
        verbose_name_plural = "Отделения"

    def __str__(self):
        return self.name
