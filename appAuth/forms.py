from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
        class Meta:
                model = User
                fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''


class UpdateProfileForm(forms.ModelForm):
      class Meta:
            model = User
            fields = ['first_name', 'last_name', 'email']