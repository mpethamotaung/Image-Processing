from django.test import TestCase
from django.urls import reverse
from .models import ImageColor
from io import BytesIO
from PIL import Image
from django.test import Client

class ImageViewTestCase(TestCase):

    def setUp(self):
        """
        Set up test data and a test client
        """

        self.client = Client()

        #Create a test image in memory
        self.test_image = BytesIO()
        image = Image.new("RGB", (100,100), color=(255,0,0))
        image.save(self.test_image, format='JPEG')
        self.test_image.seek(0)

        #URLs
        self.upload_url = reverse('pixels:upload_image')
        self.image_list_url = reverse('pixels:image_list')
        self.upload_success_url = reverse('pixels:upload_success')
        self.image_detials = reverse('pixels:image_details')

    def test_image_upload_valid(self):
        """
        Test successful image upload.
        """
        response = self.client.post(
            self.upload_url,
            {'image': self.test_image},
            format='multipart'
        )
        self.assertEqual(response.status_code, 302) #redirect to success page
        self.assertEqual(ImageColor.objects.count(),1) #check if uploaded image is saved
        uploaded_image = ImageColor.objects.first()
        self.assertIsNotNone(uploaded_image.hex_color) #Check if hex is calculated by util


    def test_image_upload_invalid(self):
        """
        Test image upload with no image file
        """
        response = self.client.post(self.upload_url, {})
        self.assertEqual(response.status_code,200) #Form should re-render
        self.assertContains(response, "This field is required") #Check for error message

    def test_image_list_view(self):
        """
        Test the image list view
        """
        #paper test images
        ImageColor.objects.create(image='test1.jpg', hex_color='#ffabc2')
        ImageColor.objects.create(image='test2.png', hex_color='#B2c100')

        response = self.client.get(self.image_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '#ffabc2')
        self.assertContains(response, '#B2c100')

    def test_image_detail_view(self):
        """
        Test the image detail view.
        """
        test_image = ImageColor.objects.create(image='test1.jpg', hex_color='#ffabc2')
        response = self.client.get(reverse('pixels:image_detail', args=[test_image.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '#B2c100')

    def test_upload_success_view(self):
        """
        Test the upload success view.
        """
        test_image = ImageColor.objects.create(image='test1.jpg', hex_color='ffabc2')
        response = self.client.get(self.upload_success_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '#ffabc2')