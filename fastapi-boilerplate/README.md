# FastAPI Boilerplate

A modern FastAPI application boilerplate with automatic API documentation and type validation.

## Features

- FastAPI with async support
- Automatic interactive API documentation (Swagger UI and ReDoc)
- Pydantic models for request/response validation
- Type hints throughout
- CORS support
- In-memory data storage (easily replaceable with database)
- Fast performance with async/await

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

4. Copy `.env.example` to `.env` (optional):
   ```bash
   cp .env.example .env
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
   
   Or simply:
   ```bash
   python main.py
   ```

The application will be available at `http://localhost:8000`

## Interactive Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

These interfaces allow you to test all API endpoints directly from your browser!

## API Endpoints

- `GET /` - Welcome message with available endpoints
- `GET /health` - Health check endpoint
- `GET /api/users` - Get all users
- `GET /api/users/{user_id}` - Get a specific user
- `POST /api/users` - Create a new user
- `PUT /api/users/{user_id}` - Update a user
- `DELETE /api/users/{user_id}` - Delete a user

## Example Usage

### Get all users
```bash
curl http://localhost:8000/api/users
```

### Create a user
```bash
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Johnson", "email": "alice@example.com"}'
```

### Get a specific user
```bash
curl http://localhost:8000/api/users/1
```

### Update a user
```bash
curl -X PUT http://localhost:8000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Smith", "email": "alice.smith@example.com"}'
```

### Delete a user
```bash
curl -X DELETE http://localhost:8000/api/users/1
```

## Project Structure

```
fastapi-boilerplate/
├── main.py             # Main application file
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment variables
└── README.md          # This file
```

## Why FastAPI?

- **Fast**: Very high performance, on par with NodeJS and Go
- **Easy**: Designed to be easy to use and learn
- **Robust**: Production-ready code with automatic data validation
- **Standards-based**: Based on OpenAPI and JSON Schema
- **Automatic docs**: Interactive API documentation generated automatically

## Next Steps

To extend this boilerplate:

1. Add a database (SQLAlchemy with async support)
2. Implement authentication (JWT, OAuth2)
3. Add dependency injection for database sessions
4. Create separate routers for different endpoints
5. Add background tasks with FastAPI's BackgroundTasks
6. Implement WebSocket support
7. Add unit tests with pytest and httpx
8. Set up logging and monitoring
9. Configure Docker for deployment
