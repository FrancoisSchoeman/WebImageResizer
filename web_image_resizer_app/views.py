from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from PIL import Image as ImagePIL
import io
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse

from .models import Image

import zipfile
import os

def resize_landscape(im, basewidth):
    transposed = im.transpose(ImagePIL.ROTATE_270)
    wpercent = (basewidth / float(transposed.size[0]))
    hsize = int((float(transposed.size[1]) * float(wpercent)))
    if basewidth > float(transposed.size[0]):
        img_resize = transposed.resize((basewidth, hsize), ImagePIL.BOX)
    elif basewidth < float(transposed.size[0]):
        img_resize = transposed.resize((basewidth, hsize), ImagePIL.ANTIALIAS)
    return img_resize


def resize_portrait(im, basewidth):
    wpercent = (basewidth / float(im.size[0]))
    hsize = int((float(im.size[1]) * float(wpercent)))
    if basewidth != im.size[0]:
        img_resize = im.resize((basewidth, hsize), ImagePIL.ANTIALIAS)
    return img_resize


def get_image_data(image, img_format):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    img_buffer = io.BytesIO()
    image.save(img_buffer, format=img_format)
    img_data = img_buffer.getvalue()
    return img_data

def resize_image(request):

    context = {
        'images_count': Image.objects.count(),
    }

    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
        basewidth = int(request.POST.get('basewidth', 800))
        img_format = request.POST.get('format', 'jpeg')
        use_custom_name = request.POST.get('use_custom_name', False)
        custom_name = request.POST.get('custom_name', '')
        path = os.path.join(settings.BASE_DIR, 'resized_images/')
        os.makedirs(path, exist_ok=True)
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            for n, image in enumerate(images):
                try:
                    im = ImagePIL.open(image)
                except OSError:
                    continue
                if im.size[0] < im.size[1]:
                    img_resize = resize_landscape(im, basewidth)
                    final_img = img_resize.transpose(ImagePIL.ROTATE_90)
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif im.size[0] > im.size[1] or im.size[0] == im.size[1]:
                    img_resize = resize_portrait(im, basewidth)
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'bmp':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'eps':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'gif':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'ico':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'jpeg':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'jpe':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'pcx':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'pdf':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'png':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'ppm':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'sgi':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'tga':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'tiff':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                elif img_format == 'webp':
                    img_resize = im
                    if use_custom_name == "on":
                        filename = f'{custom_name}_{n}.{img_format}'
                    else:
                        filename = f'{image.name.split(".")[0]}_resized.{img_format}'
                else:
                    raise ValueError('Unsupported image format')
                img_data = get_image_data(img_resize, img_format)
                zip_file.writestr(filename, img_data)
                # Create a new Image object and save it to the database
                new_image = Image(image_name=filename)
                new_image.save()
        zip_buffer.seek(0)
        response = HttpResponse(zip_buffer, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="resized_images.zip"'
        return response
    return render(request, 'index.html', context)


def contact(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'New Contact Form Submission on Image Resizer',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,
            ['francois@gardenrouteandkleinkaroo.co.za'],
            fail_silently=False,
        )

        context['success'] = "Thank you for your message. We will get back to you as soon as possible."

        return render(request, 'contact.html', context)

    return render(request, 'contact.html', context)