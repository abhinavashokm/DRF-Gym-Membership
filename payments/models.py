from django.db import models
from memberships.models import MembershipPlan
from django.conf import settings

class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        SUCCESS = 'success'
        FAILED  = 'failed'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=15, choices=PaymentStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " - " + self.plan.name + " - " + str(self.created_at.date())