# Generated by Django 3.1.4 on 2023-02-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0007_course_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="cover",
            field=models.ImageField(blank=True, upload_to="course_covers/%Y/%m/%d"),
        ),
    ]