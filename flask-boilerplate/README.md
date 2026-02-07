# Flask Boilerplate

A simple Flask application boilerplate with basic REST API endpoints.

## Features

- Basic Flask application structure
- REST API endpoints with JSON responses
- CORS support
- Environment variable configuration
- Error handling
- Health check endpoint

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

5. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`

## API Endpoints

- `GET /` - Welcome message with available endpoints
- `GET /api/health` - Health check endpoint
- `GET /api/users` - Get all users (mock data)
- `POST /api/users` - Create a new user

## Example Usage

### Get all users
```bash
curl http://localhost:5000/api/users
```

### Create a user
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Johnson", "email": "alice@example.com"}'
```

## Project Structure

```
flask-boilerplate/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment variables
└── README.md          # This file
```

## Next Steps

To extend this boilerplate:

1. Add a database (SQLAlchemy for ORM)
2. Implement authentication (Flask-JWT-Extended)
3. Add input validation (Flask-Marshmallow)
4. Create a blueprints structure for larger applications
5. Add unit tests with pytest
6. Set up a proper logging system
