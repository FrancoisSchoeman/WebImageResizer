from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse
import os
from dotenv import load_dotenv

from .image_resizer import archive_images
from .models import Image

load_dotenv()


def resize_image(request: HttpRequest) -> HttpResponse:
    """
    Handle image upload, resize images based on the specified target width, and return a zip file containing the resized images.

    Args:
        request (HttpRequest): The HTTP request object containing image files and form data.

    Returns:
        HttpResponse: A response containing a zip file with the resized images or the rendered HTML page.
    """
    context = {
        "images_count": Image.objects.count(),
    }

    if request.method == "POST" and request.FILES.getlist("images"):
        images = request.FILES.getlist("images")
        target_width = int(request.POST.get("target_width", 800))
        img_format = request.POST.get("format", "jpeg")
        use_custom_name = request.POST.get("use_custom_name", False)
        custom_name = request.POST.get("custom_name", "")
        path = os.path.join(settings.BASE_DIR, "resized_images/")
        os.makedirs(path, exist_ok=True)

        zip_buffer = archive_images(images, target_width, img_format, use_custom_name, custom_name)
        zip_buffer.seek(0)

        response = HttpResponse(zip_buffer, content_type="application/zip")
        response["Content-Disposition"] = 'attachment; filename="resized_images.zip"'
        return response
    
    return render(request, "index.html", context)


def contact(request: HttpRequest) -> HttpResponse:
    """
    Handle the contact form submission and send an email with the form details.

    Args:
        request (HttpRequest): The HTTP request object containing form data.

    Returns:
        HttpResponse: A response rendering the contact page with a success message if the form is submitted.
    """
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            "New Contact Form Submission on Image Resizer",
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            email,
            ["francois@gardenrouteandkleinkaroo.co.za"],
            fail_silently=False,
        )

        context[
            "success"
        ] = "Thank you for your message. We will get back to you as soon as possible."

        return render(request, "contact.html", context)

    return render(request, "contact.html", context)
