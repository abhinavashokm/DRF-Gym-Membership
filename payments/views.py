from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import CreatePaymentSerializer, ListPaymentHistorySerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Payment

# Create your views here.
class ListPaymentHistoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        payment_history = Payment.objects.filter(user_id=1)
        serializer = ListPaymentHistorySerializer(payment_history, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CreatePaymentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreatePaymentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({"message": "payment completed"}, status=status.HTTP_201_CREATED)
    
class CheckPaymentStatusView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        try:
            payment = Payment.objects.get(id=id)
        except KeyError:
            return Response({'message': 'invalid key'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListPaymentHistorySerializer(payment)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
