# Generated by Django 4.1.7 on 2023-03-08 09:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("app", "0002_alter_specialist_guid_and_more")]

    operations = [migrations.RemoveField(model_name="service", name="position")]
