from django.shortcuts import render,redirect
from .forms import ImageUploadForm
from .models import ImageColor
from .utils import get_center_hex


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
                return redirect('image_list')
            except ValueError as e:
                #This to inform the user if processing fails
                form.add_error(f'Failed to upload image', {'image': image})
    else:
        form = ImageUploadForm()
    #Render the uploaded image with the form
    return render(request, 'pixels/upload.html', {'form': form})

def image_list(request):
    images = ImageColor.objects.all()
    return render(request, 'pixels/image_list.html', {'images': images})

def image_detail(request, pk):
    image = ImageColor.objects.get(pk=pk)
    return render(request, 'pixels/image_details.html', {'image': image})



