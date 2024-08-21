from django import forms
from . import models
import re
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import SetPasswordForm

class RegistrationForm(forms.ModelForm):
        confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
        class Meta:
                model = models.User
                fields = ['username', 'first_name', 'last_name', 'email', 'image', 'password', 'confirm_password']
                widgets = {
                      'password':forms.PasswordInput(),
                }
        
        def clean_password(self):
              password = self.cleaned_data.get('password')

              if len(password) < 8:
                    raise ValidationError("Password must be at least 8 characters.")
              if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password) or not re.search(r"[^\w\s]", password):
                    raise ValidationError("Password must contain at least letters, digits, and symbols.")
              
              
              return password
        

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')

            if password and confirm_password and password != confirm_password:
                raise ValidationError("Passwords do not match.")

            return cleaned_data



class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''


class UpdateProfileForm(forms.ModelForm):
      class Meta:
            model = models.User
            fields = ['first_name', 'last_name', 'email']