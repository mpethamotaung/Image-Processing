from rest_framework import serializers
from .models import ImageColor

class UploadedImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageColor
        fields = ['pk', 'image', 'hex_color']
