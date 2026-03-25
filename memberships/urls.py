from django.urls import path
from .views import CreateMembershipPlanView, ListMembershipPlansView

urlpatterns = [
    path('create/', CreateMembershipPlanView.as_view()),
    path("list/", ListMembershipPlansView.as_view())
]