# Generated by Django 4.2.13 on 2024-06-16 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0005_alter_category_options_alter_group_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="group",
            options={"verbose_name": "Группа", "verbose_name_plural": "Группы"},
        ),
        migrations.AlterModelOptions(
            name="resource",
            options={
                "default_related_name": "resources",
                "ordering": ["-pub_datetime"],
                "verbose_name": "Ресурс",
                "verbose_name_plural": "Ресурсы",
            },
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Тэг", "verbose_name_plural": "Тэги"},
        ),
    ]