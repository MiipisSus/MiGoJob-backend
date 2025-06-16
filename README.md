# MiGoJob Backend

This is the backend service for the **MiGoJob** project, providing RESTful APIs and business logic for job management.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [License](#license)

## Features

- User authentication and authorization
- Job posting and management
- Company posting and management
- Admin dashboard endpoints

## Tech Stack

- **Language:** Python 3.10.x
- **Framework:** Django Ninja
- **Database:** PostgreSQL
- **ORM:** Django ORM
- **Authentication:** JWT

## Getting Started

> Ensure your `.env` file is configured with the correct environment variables before running the container.

1. **Build the Docker image:**

   ```bash
   docker compose up --build
   ```

2. **Run database initial datas (Optional):**

   ```bash
   docker compose exec web /bin/bash
   python3 manage.py seed_data
   ```

## API Documentation

Interactive API docs available at:

- `http://localhost:8000/api/docs` (Swagger docs)
- `http://127.0.0.1:8000/admin/` (Admin site)

## License

This project is licensed under the MIT License.
