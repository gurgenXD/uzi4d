# Generated by Django 4.1.7 on 2023-03-12 14:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("app", "0019_remove_servicecategory_is_active")]

    operations = [migrations.RemoveField(model_name="service", name="is_active")]
