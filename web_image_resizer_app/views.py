import django
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from PIL import Image as ImagePIL
import io
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse

from dotenv import load_dotenv

from .models import Image

import zipfile
import os

load_dotenv()


def resize_landscape(im, target_width):
    width = float(im.size[0])
    height = float(im.size[1])

    width_ratio = target_width / width
    target_height = int((height * float(width_ratio)))
    if target_width > width:
        img_resize = im.resize((target_width, target_height), ImagePIL.BOX)
    elif target_width < width:
        img_resize = im.resize((target_width, target_height), ImagePIL.ANTIALIAS)
    return img_resize


def resize_portrait(im, target_height):
    width = float(im.size[0])
    height = float(im.size[1])

    height_ratio = target_height / height
    target_width = int((width * float(height_ratio)))

    img_resize = im.resize((target_width, target_height), ImagePIL.ANTIALIAS)
    
    return img_resize


def get_image_data(image, img_format):
    if image.mode != "RGB":
        image = image.convert("RGB")
    img_buffer = io.BytesIO()
    image.save(img_buffer, format=img_format)
    img_data = img_buffer.getvalue()
    return img_data


def resize_image(request):
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
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for n, image in enumerate(images):
                try:
                    im = ImagePIL.open(image)
                except OSError:
                    continue
                print(im.size[0], im.size[1])
                if im.size[0] < im.size[1]:
                    print("portrait")
                    img_resize = resize_portrait(im, target_width)
                    if use_custom_name == "on":
                        filename = f"{custom_name}_{n}.{img_format}"
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif im.size[0] > im.size[1] or im.size[0] == im.size[1]:
                    print("landscape")
                    img_resize = resize_landscape(im, target_width)
                    if use_custom_name == "on":
                        filename = f"{custom_name}_{n}.{img_format}"
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                else:
                    raise ValueError("Unsupported image format")
                img_data = get_image_data(img_resize, img_format)
                zip_file.writestr(filename, img_data)
                # Create a new Image object and save it to the database
                new_image = Image(image_name=filename)
                new_image.save()
        zip_buffer.seek(0)
        response = HttpResponse(zip_buffer, content_type="application/zip")
        response["Content-Disposition"] = 'attachment; filename="resized_images.zip"'
        return response
    return render(request, "index.html", context)


def contact(request):
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
