from django.urls import path
from .views import PaymentView, PaymentStatusView

urlpatterns = [
    path('create/', PaymentView.as_view()),
    path('list/', PaymentView.as_view()),
    path('check-status/<int:pk>/', PaymentStatusView.as_view()),
]