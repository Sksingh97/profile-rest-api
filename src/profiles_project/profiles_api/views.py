from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, formate=None):
        """Returns a list of ApiView features."""

        an_apiview = [
        'Uses HTTP method as function (get, post, patch, put, delete)',
        'it is similar to a traditional Django view',
        'Gives you the most controle over your logic',
        'is mapped manually to Urls'
        ]

        return Response({'message': 'hello!','an_apiview':an_apiview})
