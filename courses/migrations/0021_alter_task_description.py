# Generated by Django 4.2 on 2023-04-13 23:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0020_rename_members_attached_files_task_members_files_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=ckeditor.fields.RichTextField(max_length=100000),
        ),
    ]
