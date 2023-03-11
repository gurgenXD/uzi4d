from django.db import models
from django.urls import reverse


class Specialization(models.Model):
    """Специализация."""

    guid = models.CharField("GUID", max_length=36, primary_key=True)
    name = models.CharField("Название", max_length=30)

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.name


class Specialist(models.Model):
    """Специалист."""

    guid = models.CharField("GUID", max_length=36, primary_key=True)
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50, blank=True)
    photo = models.ImageField("Фотография", blank=True, null=True)
    start_work_date = models.DateField("Начало работы")
    education = models.TextField("Образование", blank=True)
    activity = models.TextField("Деятельность", blank=True)
    description = models.TextField("Описание", blank=True)
    titles = models.TextField("Титулы", blank=True)
    can_adult = models.BooleanField("Принимает взрослых")
    can_child = models.BooleanField("Принимает детей")
    can_online = models.BooleanField("Проводит онлайн консультацию")
    on_main = models.BooleanField("Выводить на главной")
    is_active = models.BooleanField("Активно")

    specializations = models.ManyToManyField(
        "Specialization", related_name="specialists", verbose_name="Специализации", blank=True
    )

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def education_split(self):
        """Образование."""
        return self.education.split("\n")

    def activity_split(self):
        """Деятельность."""
        return self.activity.split("\n")

    def titles_split(self):
        """Титулы."""
        return self.titles.split("\n")

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        """Полное имя врача."""
        patronymic = f" {self.patronymic}" if self.patronymic else ""
        return f"{self.surname} {self.name}" + patronymic

    def get_absolute_url(self):
        """Ссылка на специалиста."""
        return reverse("specialist", args=[self.guid])


class SpecialistCertificate(models.Model):
    """Сертификат специалиста."""

    guid = models.CharField("GUID", max_length=36, primary_key=True)
    name = models.CharField("Имя", max_length=250)
    file = models.FileField("Документ")

    specialist = models.ForeignKey(
        "Specialist",
        on_delete=models.CASCADE,
        related_name="certificates",
        verbose_name="Специалист",
    )

    def __str__(self):
        return self.name
