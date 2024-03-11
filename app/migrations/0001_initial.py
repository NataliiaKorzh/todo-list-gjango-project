# Generated by Django 5.0.3 on 2024-03-11 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField(blank=True, null=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, null=True, related_name="tasks", to="app.tag"
                    ),
                ),
            ],
        ),
    ]
