from django.urls import path
from .views import CreatePaymentView, ListPaymentHistoryView, CheckPaymentStatusView

urlpatterns = [
    path('create/', CreatePaymentView.as_view()),
    path('list/', ListPaymentHistoryView.as_view()),
    path('check-status/<int:id>/', CheckPaymentStatusView.as_view()),
]