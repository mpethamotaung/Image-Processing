from PIL import Image

def get_center_hex(image_file):
    """
    Reads an image file and calculates the average
    color of its center pixels with optimized handling.
    """
    try:
        # Open the image without unnecessary memory usage
        with Image.open(image_file) as img:
            # Ensure RGB mode for consistency
            img = img.convert("RGB")
            width, height = img.size

            # Resize large images to reduce processing time (maintains aspect ratio)
            MAX_DIMENSION = 1000  # Adjust based on expected image sizes
            if max(width, height) > MAX_DIMENSION:
                img.thumbnail((MAX_DIMENSION, MAX_DIMENSION))
                width, height = img.size  # Update dimensions after resizing

            # Extract the center-most pixels
            center_pixels = [
                img.getpixel((width // 2, height // 2)),
                img.getpixel((width // 2 - 1, height // 2)),
                img.getpixel((width // 2, height // 2 - 1)),
                img.getpixel((width // 2 - 1, height // 2 - 1)),
            ]

            # Calculate the average color of the center pixels
            avg_color = tuple(
                sum(pixel[i] for pixel in center_pixels) // len(center_pixels)
                for i in range(3)  # Loop through 3 channels RGB
            )

            # Convert the average color to a hex string
            return "#{:02x}{:02x}{:02x}".format(*avg_color)

    except Exception as e:
        # Log the error for debugging and raise a custom exception
        print(f"Error processing image: {e}")  # Consider replacing with proper logging
        raise ValueError("Failed to process image. Please try again with a valid image file.")
