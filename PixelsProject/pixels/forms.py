from django import forms
from .models import ImageColor

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageColor
        fields = ['image']