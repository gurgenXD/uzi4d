# Generated by Django 4.1.7 on 2023-03-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0009_alter_rating_photo_alter_rating_reviews_count")]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="link",
            field=models.URLField(default=1, max_length=255, verbose_name="Ссылка"),
            preserve_default=False,
        )
    ]