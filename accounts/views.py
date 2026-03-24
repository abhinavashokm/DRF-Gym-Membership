from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer
from rest_framework import status

@api_view
def registerAPI(request):
    serializer = RegisterSerializer(request.data)

    if not serializer.is_valid():
        return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response({'message': "Register Successfull"}, status=status.HTTP_201_CREATED)



