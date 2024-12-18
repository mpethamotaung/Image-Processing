from rest_framework import serializers
from .models import ImageColor

class UploadedImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageColor
        fields = ['pk', 'image', 'hex_color'] 
        
        # We can also use fields = '__all__' to obtain all model fields
        """
        Used pk(primary key) instead in case we want to change the primary key
        to another field (e.g, uuid, slug). pk will still refer to the primary key
        but if we use id, we would have to rewrite the code.
        """
