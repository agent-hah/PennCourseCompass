# PennCourseCompass

Backend boilerplate code collection for Python web frameworks.

## Available Boilerplates

This repository contains production-ready boilerplate code for popular Python backend frameworks:

### 1. Flask Boilerplate (`flask-boilerplate/`)

A lightweight Flask application with REST API endpoints.

**Features:**
- Basic Flask application structure
- REST API with JSON responses
- CORS support
- Environment variable configuration
- Error handling

**Quick Start:**
```bash
cd flask-boilerplate
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

See [flask-boilerplate/README.md](flask-boilerplate/README.md) for detailed documentation.

---

### 2. Django Boilerplate (`django-boilerplate/`)

A full-featured Django REST Framework application with admin interface.

**Features:**
- Django 5.0 with Django REST Framework
- RESTful API with ViewSets
- Admin interface
- ORM models and migrations
- CORS support

**Quick Start:**
```bash
cd django-boilerplate
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

See [django-boilerplate/README.md](django-boilerplate/README.md) for detailed documentation.

---

### 3. FastAPI Boilerplate (`fastapi-boilerplate/`)

A modern, fast FastAPI application with automatic documentation.

**Features:**
- High-performance async API
- Automatic interactive documentation (Swagger UI)
- Type validation with Pydantic
- Modern Python with type hints
- CORS support

**Quick Start:**
```bash
cd fastapi-boilerplate
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

See [fastapi-boilerplate/README.md](fastapi-boilerplate/README.md) for detailed documentation.

---

## Choosing a Framework

| Framework | Best For | Performance | Learning Curve |
|-----------|----------|-------------|----------------|
| **Flask** | Small to medium projects, APIs, microservices | Good | Easy |
| **Django** | Full-stack applications, admin panels, complex projects | Good | Moderate |
| **FastAPI** | Modern APIs, microservices, high-performance apps | Excellent | Easy-Moderate |

## Common Features

All boilerplates include:
- ✅ REST API endpoints with CRUD operations
- ✅ Health check endpoint
- ✅ CORS configuration
- ✅ Environment variable support
- ✅ Example user model/endpoints
- ✅ Comprehensive documentation
- ✅ Production-ready structure

## Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

See [LICENSE](LICENSE) file for details.