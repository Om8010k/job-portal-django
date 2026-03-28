from rest_framework.permissions import BasePermission


class IsEmployer(BasePermission):
    """
    Only employers allowed
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "employer"


class IsCandidate(BasePermission):
    """
    Only candidates allowed
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "candidate"