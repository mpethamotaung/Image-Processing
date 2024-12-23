from django.shortcuts import render,redirect, get_object_or_404
from .forms import ImageUploadForm
from .models import ImageColor
from .utils import get_center_hex
from django.db import transaction

#Image Upload 
@transaction.atomic
def upload_image(request):
    """
    Handles image uploads and process the center-most pixel color
    """
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():

            image = form.cleaned_data['image']

            try:
                #Call the utility function to get center hex color
                hex_color = get_center_hex(image)
                #save the image and its hex value in db
                image_instance = ImageColor.objects.create(image=image, hex_color=hex_color)
                image_instance.save()
                #Redicrect to image list page
                return redirect('pixels:upload_success')
            except ValueError as e:
                #This to inform the user if processing fails
                form.add_error(None, 'Failed to upload image')
    else:
        form = ImageUploadForm()
    #Render the uploaded image with the form
    return render(request, 'pixels/upload_image.html', {'form': form})

# List uploaded images
def image_list(request):
    """
    Displays a list of uploaded images and their extracted hex colors.
    """
    images = ImageColor.objects.all()
    return render(request, 'pixels/image_list.html', {'images': images})

# Show image details
def image_details(request, pk):
    """
    Displays image details
    """
    image = ImageColor.objects.get(pk=pk)
    return render(request, 'pixels/image_details.html', {'image': image})

# Successful image upload
def upload_success(request):
    """
    Displays uploaded image with hex color
    """
    
    #Retrieve recent uploaded image
    image_instance = ImageColor.objects.latest('id')

    return render(request, 'pixels/upload_success.html', {'image_instance': image_instance})

#Delete uploaded image
def delete_image(request,pk):
    """
    Allows the user to delete an image
    """
    image_instance = get_object_or_404(ImageColor, pk=pk)
    
    if request.method == 'POST':
        image_instance.delete()
        return redirect('pixels:image_list')
    
    return render(request, 'pixels/confirm_delete.html', {'image': image_instance})
