# Generated by Django 4.1.7 on 2023-02-24 15:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20230224_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=10000),
        ),
    ]
