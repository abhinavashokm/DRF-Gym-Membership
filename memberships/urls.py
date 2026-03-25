from django.urls import path
from .views import CreateMembershipPlanView, ListMembershipPlansView, CheckUserMembershipStatusView

urlpatterns = [
    path('create/', CreateMembershipPlanView.as_view()),
    path("list/", ListMembershipPlansView.as_view()),
    path("check-status/<int:id>/", CheckUserMembershipStatusView.as_view())
]