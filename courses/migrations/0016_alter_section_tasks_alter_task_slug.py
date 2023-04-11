# Generated by Django 4.1.7 on 2023-03-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0015_alter_course_description_alter_task_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="section",
            name="tasks",
            field=models.ManyToManyField(blank=True, to="courses.task"),
        ),
        migrations.AlterField(
            model_name="task",
            name="slug",
            field=models.SlugField(blank=True),
        ),
    ]
