from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """"Test API view"""
    def get(self, request, format=None):
        """Returns a list o APIView features """
        an_apiview = [
            "Uses HTTP methdos as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django view",
            "Gives you the most control over you application logic",
            "Is mapped manually to URL"
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
