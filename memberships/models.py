from django.db import models
from django.conf import settings

# Create your models here.
class MembershipPlan(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name
    

class UserMembership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)