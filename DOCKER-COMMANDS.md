# Docker Commands for Production Environment

This document outlines the necessary Docker commands to manage the application in a production environment using `docker-compose.prod.yml`.

## Starting the Application

To start all services defined in the production Docker Compose file in detached mode and build containers that have changed:

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

The website will run on port 1337. You can access it at `http://localhost:1337/`.

## Database Migrations

After starting the services, you may need to make and apply database migrations. The following commands handle these operations without interactive input:

- **Make Migrations:** Analyzes the current state of the models and produces migration files for any changes detected.

  ```bash
  docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --no-input
  ```

- **Apply Migrations:** Applies the migration files, updating the database schema to match the current models.

  ```bash
  docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --no-input
  ```

## Static Files

Collect static files into a single location to serve them easily in production. This command also clears the existing static files before collecting them again:

```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

## Stopping the Application

To stop and remove all containers, networks, and volumes associated with the application in the production environment:

```bash
docker-compose -f docker-compose.prod.yml down -v
```

This command ensures a clean state for the next deployment or shutdown of the application.
