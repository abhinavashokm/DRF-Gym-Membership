from django.urls import path
from .views import PaymentView, PaymentStatusView

urlpatterns = [
    path('', PaymentView.as_view()),
    path('<int:pk>/', PaymentStatusView.as_view()),
]