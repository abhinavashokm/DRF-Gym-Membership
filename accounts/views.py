from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer, ListAccountsSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .models import User

# @api_view(['POST'])
# def registerAPI(request):
#     serializer = RegisterSerializer(data=request.data)

#     if not serializer.is_valid():
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     serializer.save()
#     return Response({'message': "Register Successfull"}, status=status.HTTP_201_CREATED)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])

        if not user:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"username": user.username, "token": str(token)}, status=status.HTTP_200_OK)

class ListAccountsView(APIView):
    def get(self, request):
        users = User.objects.filter(role=User.Role.MEMBER)
        serializer = ListAccountsSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



