from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import CreatePaymentSerializer, ListPaymentHistorySerializer
from .models import Payment
from drf_spectacular.utils import extend_schema


@extend_schema(
    description="Retrieve the authenticated user's payment history (GET) or create a new payment for a selected membership plan (POST). Creating a payment activates or extends the user's membership based on existing status."
)
class PaymentView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreatePaymentSerializer
        return ListPaymentHistorySerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


@extend_schema(
    description="Retrieve details and status of a specific payment by its ID. Typically used to check whether a payment was successful or failed."
)
class PaymentStatusView(RetrieveAPIView):
    serializer_class = ListPaymentHistorySerializer
    queryset = Payment.objects.all()
