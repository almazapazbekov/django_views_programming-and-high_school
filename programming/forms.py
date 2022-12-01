from django import forms

from .models import Student, Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'  # поля
        # исключения
        # exclude = ()
