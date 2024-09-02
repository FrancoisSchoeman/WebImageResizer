from django.test import TestCase
from PIL import Image as ImagePIL
from web_image_resizer_app.image_resizer import resize_landscape, resize_portrait

class ImageResizerTest(TestCase):
    """
    Test case for the image resizing utility functions.
    """

    def setUp(self):
        """
        Set up a test image instance for use in the tests.
        """
        self.portrait_image = ImagePIL.new('RGB', (1080, 1920))
        self.landscape_image = ImagePIL.new('RGB', (1920, 1080))

    def test_resize_landscape(self):
        """
        Test that the resize_landscape function correctly resizes an image to the specified width.
        """
        resized_image = resize_landscape(self.landscape_image, 960)
        self.assertEqual(resized_image.size, (960, 540))

    def test_resize_portrait(self):
        """
        Test that the resize_portrait function correctly resizes an image to the specified height.
        """
        resized_image = resize_portrait(self.portrait_image, 960)
        self.assertEqual(resized_image.size, (540, 960))