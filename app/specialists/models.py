from django.db import models


class Specialization(models.Model):
    guid = models.CharField("GUID 1C", max_length=36, primary_key=True)
    name = models.CharField("Название", max_length=30)

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self) -> str:
        return self.name


class Specialist(models.Model):
    guid = models.CharField("GUID 1C", max_length=36, primary_key=True)
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50, blank=True, null=True)
    photo = models.ImageField("Фотография", blank=True, null=True)
    start_work_date = models.DateField("Начало работы")
    education = models.TextField("Образование", blank=True, null=True)
    activity = models.TextField("Деятельность", blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    titles = models.TextField("Титулы", blank=True, null=True)
    can_adult = models.BooleanField("Принимает взрослых")
    can_child = models.BooleanField("Принимает детей")
    can_online = models.BooleanField("Проводит онлайн консультацию")
    on_main = models.BooleanField("Выводить на главной")
    is_active = models.BooleanField("Активно")

    specializations = models.ManyToManyField(
        "Specialization", related_name="specialists", verbose_name="Специализации"
    )

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self) -> str:
        patronymic = f" {self.patronymic}" if self.patronymic else ""
        return f"{self.surname} {self.name}" + patronymic


class SpecialistCertificate(models.Model):
    guid = models.CharField("GUID 1C", max_length=36, primary_key=True)
    name = models.CharField("Имя", max_length=250)
    file = models.FileField("Документ")

    specialist = models.ForeignKey(
        "Specialist",
        on_delete=models.CASCADE,
        related_name="certificates",
        verbose_name="Специалист",
    )

    def __str__(self) -> str:
        return self.name
