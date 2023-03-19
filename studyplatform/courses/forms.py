from django import forms
from .models import Course
from users.models import User
from ckeditor.widgets import CKEditorWidget


# rename into createcoursemodelform
class CourseCreateModelForm(forms.ModelForm):
    description = CKEditorWidget(config_name='create_course_form_description')

    class Meta:
        model = Course
        fields = ['title', 'description', 'is_active']
        labels = {
            "is_active": "Activate",
        }

        # widgets = {
        #     'description': forms.Textarea(attrs={'placeholder': 'sds'})
        # }
