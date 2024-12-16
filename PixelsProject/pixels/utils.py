from PIL import Image
from io import BytesIO

def get_center_hex(image_file):
    """
    Reads an image file and calculates the average
    color of its center pixels.
    """
    try:
        with Image.open(BytesIO(image_file.read())) as img:
            img = img.convert("RGB")
            width,height = img.size

            #Extract center-most pixels
            center_pixels = [
                img.getpixel((width // 2, height // 2)),
                img.getpixel((width // 2 - 1, height // 2)),
                img.getpixel((width // 2, height // 2 - 1)),
                img.getpixel((width // 2 - 1, height // 2 - 1)),
            ]

            #Calculate the average color
            avg_color = tuple(
                sum(pixel[i] for pixel in center_pixels) // len(center_pixels)
                for i in range(4)
            )

            #Convert to hex
            return "#{:02x}{:02x}{:02x}".format(*avg_color)
    except Exception as e:
        raise ValueError(f"Failed to process image")
        