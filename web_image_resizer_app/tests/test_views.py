import os
from django.test import TestCase, Client
from django.urls import reverse
from web_image_resizer_app.models import Image

class ImageResizerViewTest(TestCase):
    """
    Test case for the image resizer view.
    """

    def setUp(self):
        """
        Set up the test client, URL, and a test image name and path instance for use in the tests.
        """
        self.client = Client()
        self.url = reverse('resize_image')
        self.image = Image.objects.create(
            image_name="test_image.jpg",
        )
        self.image_path = os.path.join(os.path.dirname(__file__), 'test_image.jpg')

    def test_resize_image_view_get(self):
        """
        Test that the GET request to the resize image view returns a 200 status code
        and uses the correct template.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_resize_image_view_post(self):
        """
        Test that the POST request to the resize image view returns a 200 status code
        when an image is uploaded.
        """
        with open(self.image_path, 'rb') as img:
            response = self.client.post(self.url, {'image': img})

        self.assertEqual(response.status_code, 200)