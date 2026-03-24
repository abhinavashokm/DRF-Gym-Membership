from django.urls import path
from .views import registerAPI

urlpatterns = [
    path('', registerAPI)
]