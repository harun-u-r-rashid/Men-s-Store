from django import forms
from .models import Review


class ProductReviewForm(forms.ModelForm):
        class Meta:
                model = Review
                fields = ['rating', 'review']

                
                