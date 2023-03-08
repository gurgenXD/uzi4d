# Generated by Django 4.1.7 on 2023-03-08 08:52

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="specialist",
            name="guid",
            field=models.CharField(
                max_length=36, primary_key=True, serialize=False, verbose_name="GUID"
            ),
        ),
        migrations.AlterField(
            model_name="specialistcertificate",
            name="guid",
            field=models.CharField(
                max_length=36, primary_key=True, serialize=False, verbose_name="GUID"
            ),
        ),
        migrations.AlterField(
            model_name="specialization",
            name="guid",
            field=models.CharField(
                max_length=36, primary_key=True, serialize=False, verbose_name="GUID"
            ),
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "position",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Позиция"),
                ),
                (
                    "guid",
                    models.CharField(
                        max_length=36, primary_key=True, serialize=False, verbose_name="GUID"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "short_description",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="Короткое описание"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Короткое описание"),
                ),
                ("is_group", models.BooleanField(verbose_name="Группа")),
                ("is_active", models.BooleanField(verbose_name="Активно")),
                ("on_main", models.BooleanField(verbose_name="Показывать на главной")),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="app.service",
                        verbose_name="GUID родителя",
                    ),
                ),
            ],
            options={"verbose_name": "Услуга", "verbose_name_plural": "Услуги"},
        ),
    ]