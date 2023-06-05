from django.db import models

# Create a model that stores the number of images resized
class Image(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    image_name = models.CharField(max_length=100)

    def __str__(self):
        return self.image_name