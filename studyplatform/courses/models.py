from django.db import models

from django.utils.text import slugify
from ckeditor.fields import RichTextField

from users.models import User

class Course(models.Model):
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=False, null=False)
    description = RichTextField(
        blank=True, max_length=10000, config_name='create_course_form_description')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    # password = models.CharField(blank=True, max_length=50)
    cover = models.ImageField(
        default='default/default_course_cover.jpeg', upload_to='course_covers/%Y/%m/%d/', blank=True, max_length=255)

    # вирішити чи буду я видаляти і сам об'єкт в базі після видалення з списку, чи ні

    members = models.ManyToManyField(
        "users.User", related_name='members', blank=True)
    teachers = models.ManyToManyField(
        "users.User", related_name='teachers', blank=True)
    goals = models.ManyToManyField(
        "Goal", related_name='goals', blank=True)
    sections = models.ManyToManyField('Section', blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    # i don't link it with course owner, because I will have other teachers create sections
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    tasks = models.ManyToManyField('Task', blank=True)
    slug = models.SlugField(null=False)

    def __str__(self):
        return self.title


class Task(models.Model):
    # i don't link it with course owner, because I will have other teachers create tasks
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=20)
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=False, blank=True)
    description = RichTextField(max_length=10000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # dead_line = models.DateTimeField(default=)
    active = models.BooleanField(default=True)
    task_files = models.FileField(blank=True)
    members_can_attach_files = models.BooleanField(default=False)
    members_attached_files = models.FileField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + '-' + str(self.pk))
        return super().save(*args, **kwargs)


class Goal(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=1000, blank=True)
    # icon = models.ImageField(upload_to='icons/user_icons')

    def __str__(self):
        return self.title
