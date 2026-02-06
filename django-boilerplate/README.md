# Django Boilerplate

A Django REST Framework application boilerplate with basic CRUD API endpoints.

## Features

- Django 5.0 with Django REST Framework
- RESTful API with ViewSets
- CORS support
- Admin interface
- SQLite database (easily switchable to PostgreSQL/MySQL)
- Environment variable configuration
- User model example with CRUD operations

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and configure your environment variables:
   ```bash
   cp .env.example .env
   ```

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000`
Admin interface at `http://localhost:8000/admin`

## API Endpoints

- `GET /api/` - Welcome message with available endpoints
- `GET /api/health/` - Health check endpoint
- `GET /api/users/` - List all users
- `POST /api/users/` - Create a new user
- `GET /api/users/{id}/` - Get a specific user
- `PUT /api/users/{id}/` - Update a user
- `PATCH /api/users/{id}/` - Partially update a user
- `DELETE /api/users/{id}/` - Delete a user

## Example Usage

### List all users
```bash
curl http://localhost:8000/api/users/
```

### Create a user
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Johnson", "email": "alice@example.com"}'
```

### Get a specific user
```bash
curl http://localhost:8000/api/users/1/
```

### Update a user
```bash
curl -X PUT http://localhost:8000/api/users/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Smith", "email": "alice.smith@example.com"}'
```

### Delete a user
```bash
curl -X DELETE http://localhost:8000/api/users/1/
```

## Project Structure

```
django-boilerplate/
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment variables
├── myproject/         # Project configuration
│   ├── settings.py    # Django settings
│   ├── urls.py        # URL configuration
│   ├── wsgi.py        # WSGI configuration
│   └── asgi.py        # ASGI configuration
└── myapp/             # Example app
    ├── models.py      # Database models
    ├── serializers.py # DRF serializers
    ├── views.py       # API views
    ├── urls.py        # App URLs
    └── admin.py       # Admin configuration
```

## Next Steps

To extend this boilerplate:

1. Add authentication (JWT, OAuth, etc.)
2. Add more models and relationships
3. Implement pagination and filtering
4. Add permissions and user roles
5. Set up PostgreSQL or MySQL database
6. Add unit tests with Django's test framework
7. Configure static files and media uploads
8. Set up Celery for background tasks
9. Add API documentation with drf-spectacular
