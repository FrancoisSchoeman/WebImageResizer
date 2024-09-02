from django.test import TestCase
from web_image_resizer_app.models import Image

class ImageModelTest(TestCase):
    """
    Test case for the Image model.
    """

    def setUp(self):
        """
        Set up a test image instance for use in the tests.
        """
        self.image = Image.objects.create(
            image_name="test_image.jpg"
        )

    def test_image_creation(self):
        """
        Test that an Image instance is created correctly.
        """
        self.assertIsInstance(self.image, Image)
        self.assertEqual(self.image.image_name, "test_image.jpg")