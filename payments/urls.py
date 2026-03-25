from django.urls import path
from .views import CreatePayment

urlpatterns = [
    path('create/', CreatePayment.as_view())
]