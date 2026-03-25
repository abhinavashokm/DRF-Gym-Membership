from rest_framework.permissions import BasePermission
from .models import User

class IsGymOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.OWNER