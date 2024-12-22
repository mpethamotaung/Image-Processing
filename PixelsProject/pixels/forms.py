from django import forms
from .models import ImageColor
from django.core.exceptions import ValidationError
from PIL import Image 

class ImageUploadForm(forms.ModelForm):

    MAX_FILE_SIZE = 5 * 1024 * 1024 #5mb 
    
    
    class Meta:
        model = ImageColor
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        
        #Check for file size
        if image.size > self.MAX_FILE_SIZE:
            raise ValidationError(f"The file is too large. The maximum file size is {self.MAX_FILE_SIZE/(1024*1024)} MB.")

        #Verify image
        try:
            img = Image.open(image)
            img.verify()
        except Exception:
            raise ValidationError("Please upload a valid image file")
        
        return image