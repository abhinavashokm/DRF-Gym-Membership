from rest_framework import serializers
from .models import MembershipPlan

class ListMembershipPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = MembershipPlan
        fields = ['id', 'name', 'price', 'duration_days']

class CreateMembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = '__all__'

    