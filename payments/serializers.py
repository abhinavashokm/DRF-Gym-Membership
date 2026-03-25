from rest_framework import serializers
from .models import Payment
from memberships.models import UserMembership, MembershipPlan
from accounts.models import User
from datetime import date, timedelta

class ListPaymentHistorySerializer(serializers.ModelSerializer):
    plan = serializers.CharField(source='plan.name')

    class Meta:
        model = Payment
        fields = ['amount', 'status','plan', 'created_at']


class CreatePaymentSerializer(serializers.Serializer):
    plan_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def validate(self, attrs):
        if not MembershipPlan.objects.filter(id=attrs["plan_id"]).exists():
            raise serializers.ValidationError("Given Plan does not exists!")

        return attrs

    def create(self, validated_data):
        user = User.objects.get(id=validated_data["user_id"])
        plan = MembershipPlan.objects.get(id=validated_data["plan_id"])

        payment = Payment.objects.create(
            user=user,
            plan=plan,
            amount=plan.price,
            status=Payment.PaymentStatus.SUCCESS,
        )
        today = date.today()

        membership, created = UserMembership.objects.get_or_create(
            user=user,
            defaults={
                "plan": plan,
                "start_date": today,
                "end_date": today + timedelta(days=plan.duration_days),
            }
        )

        if not created:
            if membership.end_date > today:
                membership.end_date += timedelta(days=plan.duration_days)
            else:
                membership.start_date = today
                membership.end_date = today + timedelta(days=plan.duration_days)

            membership.plan = plan
            membership.is_active = True
            membership.save()

        return payment
