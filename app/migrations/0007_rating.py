# Generated by Django 4.1.7 on 2023-03-11 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0006_promotion_alter_updater_start_update")]

    operations = [
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Источник")),
                ("score", models.CharField(max_length=3, verbose_name="Рейтинг")),
                ("reviews_count", models.TextField(blank=True, verbose_name="Описание")),
                ("photo", models.ImageField(upload_to="", verbose_name="Фото")),
            ],
            options={"verbose_name": "Рейтинг", "verbose_name_plural": "Рейтинги"},
        )
    ]
