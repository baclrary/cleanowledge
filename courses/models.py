from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from users.models import User


class Course(models.Model):
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=False, null=False)
    description = RichTextField(blank=True, max_length=10000, config_name="create_course_form_description")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    # password = models.CharField(blank=True, max_length=50)
    cover = models.ImageField(
        default="default/default_course_cover.jpeg", upload_to="course_covers/%Y/%m/%d/", blank=True, max_length=255
    )

    members = models.ManyToManyField("users.User", related_name="members", blank=True)
    teachers = models.ManyToManyField("users.User", related_name="teachers", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"pk": self.pk})


class Section(models.Model):
    # number_in_course = models.IntegerField()

    # I don't link it with course owner, because I will have other teachers create sections
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=120)
    tasks = models.ManyToManyField("Task", blank=True)
    slug = models.SlugField(null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:section-detail", kwargs={"spk": self.pk, "pk": self.course.pk})


class Task(models.Model):
    TASK_TYPE_CHOICES = (
        ("article", "Article"),
        ("video", "Video"),
        ("link", "Link"),
        ("assigment", "Assigment"),
    )
    # I don't link it with course owner, because I will have other teachers create tasks
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES)
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=False, blank=True)
    description = RichTextField(max_length=100000, config_name="task_description")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # dead_line = models.DateTimeField(default=)
    active = models.BooleanField(default=True)
    task_files = models.FileField(blank=True)
    members_can_attach_files = models.BooleanField(blank=True)
    members_files = models.FileField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Save the instance temporarily to generate the primary key (pk)
        super().save(*args, **kwargs)
        self.slug = slugify(self.title + "-" + str(self.pk))
        # Save the instance again with the updated slug
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title + "-" + str(self.pk))
    #     return super().save(*args, **kwargs)


class Goal(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=1000, blank=True)

    # icon = models.ImageField(upload_to='icons/user_icons')

    def __str__(self):
        return self.title
