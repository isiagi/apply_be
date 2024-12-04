from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class PingView(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def ping(self, request):
        return Response("Pong", status=status.HTTP_200_OK)