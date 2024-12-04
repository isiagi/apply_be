from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class PingView(viewsets.ViewSet):
    def ping(self, request):
        return Response("Pong", status=status.HTTP_200_OK)