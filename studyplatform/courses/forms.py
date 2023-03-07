from django import forms
from .models import Course
from users.models import User


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            'owner',
            'title',
            'is_active',
        )


# class CourseAddTeacherModelForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', )
