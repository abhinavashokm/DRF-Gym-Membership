from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import CreateMembershipPlanSerializer, ListMembershipPlanSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import MembershipPlan

class CreateMembershipPlanView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreateMembershipPlanSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(
            {"message": "New Membership Plan Created Successfully!"},
            status=status.HTTP_201_CREATED,
        )

class ListMembershipPlansView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        plans = MembershipPlan.objects.all()
        serializer = ListMembershipPlanSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)