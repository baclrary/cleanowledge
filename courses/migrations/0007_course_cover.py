# Generated by Django 3.1.4 on 2023-02-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0006_auto_20230223_1137"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="cover",
            field=models.ImageField(blank=True, upload_to="course_covers/<django.db.models.fields.CharField>/%Y/%m/%d"),
        ),
    ]