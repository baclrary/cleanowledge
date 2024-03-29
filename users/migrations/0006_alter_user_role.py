# Generated by Django 4.2 on 2023-04-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("student", "Student"), ("teacher", "Teacher"), ("admin", "Admin")],
                default="student",
                max_length=100,
            ),
        ),
    ]
