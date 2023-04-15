# Generated by Django 4.2 on 2023-04-11 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_remove_course_sections_section_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='goals',
        ),
        migrations.AddField(
            model_name='goal',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='courses.course'),
            preserve_default=False,
        ),
    ]