# Generated by Django 4.1.7 on 2023-03-08 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0003_remove_service_position")]

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Название")),
                ("is_active", models.BooleanField(verbose_name="Активно")),
            ],
            options={"verbose_name": "Город", "verbose_name_plural": "Города"},
        ),
        migrations.AlterField(
            model_name="specialist",
            name="activity",
            field=models.TextField(blank=True, default=1, verbose_name="Деятельность"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="specialist",
            name="description",
            field=models.TextField(blank=True, default=1, verbose_name="Описание"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="specialist",
            name="education",
            field=models.TextField(blank=True, default=1, verbose_name="Образование"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="specialist",
            name="patronymic",
            field=models.CharField(blank=True, default=1, max_length=50, verbose_name="Отчество"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="specialist",
            name="specializations",
            field=models.ManyToManyField(
                blank=True,
                related_name="specialists",
                to="app.specialization",
                verbose_name="Специализации",
            ),
        ),
        migrations.AlterField(
            model_name="specialist",
            name="titles",
            field=models.TextField(blank=True, default=1, verbose_name="Титулы"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="updater",
            name="error_log",
            field=models.TextField(blank=True, default=1, verbose_name="Текст ошибки"),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Office",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("description", models.CharField(max_length=100, verbose_name="Описание")),
                ("address", models.CharField(max_length=100, verbose_name="Адрес")),
                ("work_time", models.CharField(max_length=100, verbose_name="Рабочее время")),
                ("phone", models.CharField(max_length=20, verbose_name="Телефон")),
                ("email", models.CharField(max_length=30, verbose_name="E-mail")),
                ("main_doctor", models.CharField(max_length=50, verbose_name="Главный врач")),
                (
                    "main_doctor_work_time",
                    models.CharField(max_length=100, verbose_name="Приёмные часы"),
                ),
                ("coor_x", models.CharField(max_length=10, verbose_name="Координата X")),
                ("coor_y", models.CharField(max_length=10, verbose_name="Координата Y")),
                ("is_active", models.BooleanField(verbose_name="Активно")),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="offices",
                        to="app.city",
                        verbose_name="Город",
                    ),
                ),
            ],
            options={"verbose_name": "Филиал", "verbose_name_plural": "Филиалы"},
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("tags", models.CharField(blank=True, max_length=100, verbose_name="Теги")),
                (
                    "short_description",
                    models.CharField(max_length=300, verbose_name="Короткое описание"),
                ),
                ("description", models.TextField(max_length=300, verbose_name="Описание")),
                ("photo", models.ImageField(upload_to="", verbose_name="Фотография")),
                ("is_active", models.BooleanField(verbose_name="Активно")),
                (
                    "office",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departaments",
                        to="app.office",
                        verbose_name="Филиал",
                    ),
                ),
            ],
            options={"verbose_name": "Отделение", "verbose_name_plural": "Отделения"},
        ),
    ]
