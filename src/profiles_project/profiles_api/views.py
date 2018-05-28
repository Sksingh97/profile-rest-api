from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    serializers_class = serializers.HelloSerializer

    def get(self, request, formate=None):
        """Returns a list of ApiView features."""

        an_apiview = [
        'Uses HTTP method as function (get, post, patch, put, delete)',
        'it is similar to a traditional Django view',
        'Gives you the most controle over your logic',
        'is mapped manually to Urls'
        ]

        return Response({'message': 'hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello msg with our name."""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handels updating an object"""

        return Response({'method':'put'})


    def patch(sefl, request, pk=None):
        """Patch request, only updates field provided in the req."""

        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Deletes and objects."""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test api viewset."""

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses action (list, create, retrieve, update, partial_update)',
            'Automatically maps to urls using routers',
            'provides more functionality with less code.'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello msg"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrive(self, request, pk=None):
        """Handels getting an object by its id"""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handels Updating an Object."""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handels Updating part of object."""

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handels removing an object."""

        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """handles creating reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
