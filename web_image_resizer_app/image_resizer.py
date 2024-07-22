from PIL import Image as ImagePIL
import io
import zipfile
from .models import Image
from typing import List, Union


def resize_landscape(im: ImagePIL.Image, target_width: int) -> ImagePIL.Image:
    """
    Resize an image to a specified width while maintaining the aspect ratio for landscape orientation.

    Args:
        im (ImagePIL.Image): The original image.
        target_width (int): The target width for the resized image.

    Returns:
        ImagePIL.Image: The resized image.
    """
    width = float(im.size[0])
    height = float(im.size[1])

    width_ratio = target_width / width
    target_height = int((height * float(width_ratio)))
    
    if target_width > width:
        img_resize = im.resize((target_width, target_height), ImagePIL.BOX)
    elif target_width < width:
        img_resize = im.resize((target_width, target_height), ImagePIL.ANTIALIAS)
    else:
        return im
    return img_resize


def resize_portrait(im: ImagePIL.Image, target_height: int) -> ImagePIL.Image:
    """
    Resize an image to a specified height while maintaining the aspect ratio for portrait orientation.

    Args:
        im (ImagePIL.Image): The original image.
        target_height (int): The target height for the resized image.

    Returns:
        ImagePIL.Image: The resized image.
    """
    width = float(im.size[0])
    height = float(im.size[1])

    height_ratio = target_height / height
    target_width = int((width * float(height_ratio)))

    if target_width > width:
        img_resize = im.resize((target_width, target_height), ImagePIL.BOX)
    elif target_width < width:
        img_resize = im.resize((target_width, target_height), ImagePIL.ANTIALIAS)
    else:
        return im
    return img_resize


def get_image_data(image: ImagePIL.Image, img_format: str) -> bytes:
    """
    Convert an image to a specified format and return the image data as bytes.

    Args:
        image (ImagePIL.Image): The original image.
        img_format (str): The format to save the image in (e.g., 'JPEG', 'PNG').

    Returns:
        bytes: The image data in the specified format.
    """
    if image.mode != "RGB":
        image = image.convert("RGB")
    img_buffer = io.BytesIO()
    image.save(img_buffer, format=img_format)
    img_data = img_buffer.getvalue()
    return img_data


def archive_images(
    images: List[Union[str, io.BytesIO]], 
    target_width: int, 
    img_format: str, 
    use_custom_name: bool, 
    custom_name: str
) -> io.BytesIO:
    """
    Archive a list of images into a zip file after resizing them based on the specified target width.

    Args:
        images (List[Union[str, io.BytesIO]]): A list of image file paths or file-like objects.
        target_width (int): The target width for resizing the images.
        img_format (str): The format to save the images in (e.g., 'jpeg', 'png').
        use_custom_name (bool): Whether to use a custom name for the resized images.
        custom_name (str): The custom name to use if `use_custom_name` is True.

    Returns:
        io.BytesIO: A buffer containing the zip file with the resized images.
    """
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
                if use_custom_name:
                    filename = f"{custom_name}_{n}.{img_format}"
                else:
                    filename = f'{image.name.split(".")[0]}_resized.{img_format}'
            elif im.size[0] > im.size[1] or im.size[0] == im.size[1]:
                print("landscape")
                img_resize = resize_landscape(im, target_width)
                if use_custom_name:
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

    return zip_buffer