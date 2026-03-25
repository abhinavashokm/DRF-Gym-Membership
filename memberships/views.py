from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import (
    CreateMembershipPlanSerializer,
    ListMembershipPlanSerializer,
    CheckUserMembershipSerializer,
)
from .models import MembershipPlan, UserMembership
from rest_framework.exceptions import NotFound
from accounts.permissions import IsGymOwner
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


@extend_schema(
    description="Retrieve all membership plans (GET) or create a new plan (POST). Plan creation is restricted to gym owners."
)
class MembershipPlanView(ListCreateAPIView):
    queryset = MembershipPlan.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateMembershipPlanSerializer
        return ListMembershipPlanSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsGymOwner()]
        return [IsAuthenticated()]


@extend_schema(
    description="Retrieve the current authenticated user's membership details. Returns active membership information or an error if no membership exists."
)
class UserMembershipStatusView(RetrieveAPIView):
    serializer_class = CheckUserMembershipSerializer

    def get_object(self):
        try:
            return UserMembership.objects.get(user=self.request.user)
        except UserMembership.DoesNotExist:
            raise NotFound("Currently you don't have any membership in the Gym")
