# Generated by Django 4.2 on 2023-04-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0019_remove_course_goals_goal_course"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="members_attached_files",
            new_name="members_files",
        ),
        migrations.AlterField(
            model_name="task",
            name="members_can_attach_files",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="task_type",
            field=models.CharField(
                choices=[("article", "Article"), ("video", "Video"), ("link", "Link"), ("assigment", "Assigment")],
                max_length=20,
            ),
        ),
    ]
