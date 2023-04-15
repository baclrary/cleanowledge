from ckeditor.widgets import CKEditorWidget
from django import forms

from users.models import User

from .models import Course, Section, Task


# rename into createcoursemodelform
class CourseCreateModelForm(forms.ModelForm):
    description = CKEditorWidget(config_name="create_course_form_description")

    class Meta:
        model = Course
        fields = ["title", "description", "is_active"]
        labels = {
            "is_active": "Activate",
        }


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "cover", "is_active"]
        labels = {
            "is_active": "Activate",
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'description': forms.Textarea(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'rows': 4}),
            'cover': forms.FileInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'mt-1'}),
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["owner", "course", "title", "tasks", "slug"]


class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["title"]


class TaskForm(forms.ModelForm):
    # iterable
    class Meta:
        model = Task
        fields = ["task_type", 'title', 'description', 'active',
                  'task_files',
                  'members_can_attach_files',
                  'members_files', ]

        # widgets = {
        #     'description': forms.Textarea(attrs={'rows': 5}),
        # }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'description': forms.Textarea(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'rows': 4}),
            'cover': forms.FileInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'mt-1'}),
        }
