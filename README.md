# Image Resizer

Image Resizer is a Django-based web application that allows you to resize multiple images at once in various formats. It's built using Django 3.2, Bootstrap 5, and the Pillow library. This application also uses python-dotenv for handling environment variables and Docker for easy deployment and development.

## Features

- Resize multiple images at once
- Rename the images to a custom name
- Support for various image formats
- Easy-to-use interface powered by Bootstrap 5
- Docker support for easy setup and deployment

## Demo

You can view the demo here: https://francoisschoeman.pythonanywhere.com/

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Docker and Docker Compose (optional)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/FrancoisSchoeman/WebImageResizer.git
   cd WebImageResizer
   ```

2. Copy the `.env.example` file to `.env.dev` or to `.env.prod` and update the environment variables:

   ```bash
   cp .env.example .env.dev # for development
   cp .env.example .env.prod # for production
   ```

3. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

   For production, use:

   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

   For more detailed production setup instructions, refer to the [DOCKER-COMMANDS.md](DOCKER-COMMANDS.md) file.

4. Access the development application at `http://127.0.0.1:8000/`.

### Without Docker

If you prefer not to use Docker, follow these steps:

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. Run migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

## Contributing

Feel free to contribute to the project by opening issues, submitting pull requests, or providing feedback.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.
