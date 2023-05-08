from django import forms

from django.contrib.auth.forms import UserCreationForm
# default user creation
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password","password1"]