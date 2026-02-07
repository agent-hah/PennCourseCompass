from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['DEBUG'] = os.environ.get('DEBUG', 'True') == 'True'


@app.route('/')
def index():
    """
    Home endpoint
    """
    return jsonify({
        'message': 'Welcome to Flask Boilerplate API',
        'version': '1.0.0',
        'endpoints': {
            'GET /': 'This endpoint',
            'GET /api/health': 'Health check',
            'GET /api/users': 'Get all users',
            'POST /api/users': 'Create a user'
        }
    })


@app.route('/api/health')
def health():
    """
    Health check endpoint
    """
    return jsonify({
        'status': 'healthy',
        'message': 'Service is running'
    })


@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Get all users (mock data)
    """
    users = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
    ]
    return jsonify(users)


@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Create a new user
    """
    data = request.get_json()
    
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400
    
    new_user = {
        'id': 3,  # In a real app, this would be generated
        'name': data['name'],
        'email': data['email']
    }
    
    return jsonify(new_user), 201


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors
    """
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors
    """
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
