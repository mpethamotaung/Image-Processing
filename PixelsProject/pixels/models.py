from django.db import models


class ImageColor(models.Model):

    image = models.ImageField(upload_to='uploads/')
    hex_color = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.image.name} - {self.hex_color}"