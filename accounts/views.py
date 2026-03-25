from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, ListAccountsSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .models import User
from .permissions import IsGymOwner
from rest_framework.permissions import IsAuthenticated

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ListAccountsView(ListAPIView):
    serializer_class = ListAccountsSerializer
    queryset = User.objects.filter(role=User.Role.MEMBER)
    permission_classes = [IsAuthenticated, IsGymOwner]

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])

        if not user:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"username": user.username, "token": str(token)}, status=status.HTTP_200_OK)





