from PIL import Image

def get_center_hex(image_path):
    with Image.open(image_path) as img:
        img = img.convert("RBG")
        width, height = img.size
        center_pixels = [
            img.getpixel((width//2, height//2)),
            img.getpixel((width//2-1, height//2)),
            img.getpixel((width//2, height//2-1)),
            img.getpixel((width//2-1, height//2-1)),
        ]
        avg_color = tuple(
            sum(pixel[i] for pixel in center_pixels)//len(center_pixels)
            for i in range(3)
        )
        return "#{:02x}{:02x}{:02x}".format(*avg_color)