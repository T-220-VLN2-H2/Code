# Generated by Django 4.0.4 on 2022-05-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_usersales_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="description",
            field=models.TextField(max_length=1800, null=True),
        ),
    ]