from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Course, Mark


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }


class StudentCreation(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all())

    class Meta:
        model = Student
        fields = ('name', 'adm_no', 'reg_no', 'course')


class MarkCreation(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        pk1 = kwargs.pop('list1')

        super(MarkCreation, self).__init__(*args, **kwargs)
        self.fields['sub'] = forms.ModelChoiceField(queryset=pk1)

    class Meta:
        model = Mark
        fields = ('sub', 's_mark1', 's_mark2')
