# Generated by Django 4.2.13 on 2024-06-15 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0002_alter_tag_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(),
        ),
    ]