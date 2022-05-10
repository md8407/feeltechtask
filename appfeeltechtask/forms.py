from dataclasses import fields
from pyexpat import model
from django import forms
from .models import User

class Userform(forms.ModelForm):
    username  = forms.CharField(max_length=200, required=False)
    password = forms.PasswordInput()

    class Meta():
        model = User
        fields = '__all__'