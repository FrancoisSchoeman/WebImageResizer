# Image Resizer

Image Resizer is a Django-based web application that allows you to resize multiple images at once in various formats. It's built using Django 3.2, Bootstrap 5, and the Pillow library. This application also uses python-dotenv for handling environment variables.

## Features

- Resize multiple images at once
- Rename the images to a custom name
- Support for various image formats
- Easy-to-use interface powered by Bootstrap 5

## Getting Started

Follow these steps to set up the Image Resizer project on your local machine:

1. Clone the repository:

   ```
   $ git clone https://github.com/FrancoisSchoeman/WebImageResizer.git
   $ cd web_image_resizer
   ```

2. Create a virtual environment and activate it:

   ```
   $ python -m venv env
   $ source env/bin/activate
   ```

3. Install the required packages from `requirements.txt`:

   ```
   (env)$ pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory with the following variables:

   ```
   SECRET_KEY=<your_django_secret_key>
   EMAIL_HOST=<your_email_host>
   EMAIL_HOST_USER=<your_email_host_user>
   EMAIL_HOST_PASSWORD=<your_email_host_password>
   ```

   Replace the placeholder values with your own Django secret key and email settings. You can generate a new Django secret key using the following command:

   ```
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

5. Create a new `db.sqlite3` file in the project root directory.

6. Run migrations and start the development server:

   ```
   (env)$ python manage.py migrate
   (env)$ python manage.py runserver
   ```

Now you can access the Image Resizer application at `http://127.0.0.1:8000/`.

## Contributing

Feel free to contribute to the project by opening issues, submitting pull requests, or providing feedback.

## License

This project is licensed under the MIT License.
