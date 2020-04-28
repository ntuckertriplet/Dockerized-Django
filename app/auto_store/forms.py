from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm


class EmployeeCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Employee
        fields = [
            'name',
            'email',
            'password1',
            'password2',
        ]
