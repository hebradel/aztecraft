# Generated by Django 5.2 on 2025-04-15 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("usuario", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=250)),
            ],
        ),
    ]
