from ckeditor.widgets import CKEditorWidget
from django import forms

from users.models import User

from .models import Course, Section


# rename into createcoursemodelform
class CourseCreateModelForm(forms.ModelForm):
    description = CKEditorWidget(config_name="create_course_form_description")

    class Meta:
        model = Course
        fields = ["title", "description", "is_active"]
        labels = {
            "is_active": "Activate",
        }

        # widgets = {
        #     'description': forms.Textarea(attrs={'placeholder': 'sds'})
        # }


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["owner", "title", "tasks", "slug"]
