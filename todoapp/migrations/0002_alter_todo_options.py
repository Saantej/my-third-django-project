# Generated by Django 4.1.5 on 2023-01-28 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"verbose_name": "Задание", "verbose_name_plural": "Задания"},
        ),
    ]
