# Generated by Django 3.1.4 on 2023-02-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0004_course_teachers"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]