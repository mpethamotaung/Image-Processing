from django.shortcuts import render,redirect
from .forms import ImageUploadForm
from .models import ImageColor
from .utils import get_center_hex

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)

            #Pillow + BytesIO to get the hex color
            try:
                image_instance.hex_color = get_center_hex(image_instance.image)
                image_instance.save()
                return redirect('image_list')
            except ValueError as e:
                form.add_error('image', f"Image processing failed: {str(e)}")
        else:
            form = ImageUploadForm()
        return render(request, 'pixels/upload.html', {'form':form})

def image_list(request):
    images = ImageColor.objects.all()
    return render(request, 'pixels/image_list.html', {'images': images})

def image_detail(request, pk):
    image = ImageColor.objects.get(pk=pk)
    return render(request, 'pixels/image_details.html', {'image': image})



