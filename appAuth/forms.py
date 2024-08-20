from django import forms
from . import models

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import SetPasswordForm

class RegistrationForm(forms.ModelForm):
        confirm_password = forms.CharField(required=True)
        class Meta:
                model = models.User
                fields = ['username', 'first_name', 'last_name', 'email', 'image', 'password', 'confirm_password']



class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''


class UpdateProfileForm(forms.ModelForm):
      class Meta:
            model = models.User
            fields = ['first_name', 'last_name', 'email']