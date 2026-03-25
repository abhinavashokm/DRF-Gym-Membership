from rest_framework import serializers
from .models import MembershipPlan, UserMembership

class ListMembershipPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = MembershipPlan
        fields = ['id', 'name', 'price', 'duration_days']

class CreateMembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = '__all__'

class CheckUserMembershipSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    current_plan = serializers.CharField(source='plan.name')
    class Meta:
        model = UserMembership
        fields = ['username', 'current_plan', 'start_date', 'end_date']