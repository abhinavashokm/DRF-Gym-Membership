from django.urls import path
from .views import RegisterView, LoginView, ListAccountsView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('list/', ListAccountsView.as_view())
]