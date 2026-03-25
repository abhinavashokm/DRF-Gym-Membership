from django.urls import path
from .views import MembershipPlanView, UserMembershipStatusView

urlpatterns = [
    path('create/', MembershipPlanView.as_view()),
    path("list/", MembershipPlanView.as_view()),
    path("status/", UserMembershipStatusView.as_view())
]