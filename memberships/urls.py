from django.urls import path
from .views import MembershipPlanView, UserMembershipStatusView

urlpatterns = [
    path('', MembershipPlanView.as_view()),
    path("me/", UserMembershipStatusView.as_view())
]