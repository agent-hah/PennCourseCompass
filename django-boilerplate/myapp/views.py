from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def index(request):
    """
    API root endpoint
    """
    return Response({
        'message': 'Welcome to Django REST API Boilerplate',
        'version': '1.0.0',
        'endpoints': {
            'GET /api/': 'This endpoint',
            'GET /api/health/': 'Health check',
            'GET /api/users/': 'List all users',
            'POST /api/users/': 'Create a user',
            'GET /api/users/{id}/': 'Get a specific user',
            'PUT /api/users/{id}/': 'Update a user',
            'DELETE /api/users/{id}/': 'Delete a user'
        }
    })


@api_view(['GET'])
def health(request):
    """
    Health check endpoint
    """
    return Response({
        'status': 'healthy',
        'message': 'Service is running'
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model
    Provides CRUD operations for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
