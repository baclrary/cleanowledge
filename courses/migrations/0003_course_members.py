# Generated by Django 4.1.4 on 2022-12-25 19:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0002_course_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="members",
            field=models.ManyToManyField(blank=True, related_name="members", to=settings.AUTH_USER_MODEL),
        ),
    ]