from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import CreatePaymentSerializer, ListPaymentHistorySerializer

from .models import Payment

class PaymentView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePaymentSerializer
        return ListPaymentHistorySerializer
    
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

class PaymentStatusView(RetrieveAPIView):
    serializer_class = ListPaymentHistorySerializer
    queryset = Payment.objects.all()
    