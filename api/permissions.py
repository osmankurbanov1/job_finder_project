from rest_framework import permissions
from company_app.models import Company


class IsAuthenticatedAndHasNotResume(permissions.BasePermission):
    """
    Allows access only to authenticated users without Resume.
    """

    def has_permission(self, request, view):
        try:
            return bool(request.user and request.user.is_authenticated and not request.user.resumes)
        except:
            return True


class IsAuthenticatedAndHasTheResume(permissions.BasePermission):
    """
    Allows access only to authenticated users to update their Resume.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAuthenticatedAndHaveNotCompanyOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if request.user.is_authenticated and request.user.companies:
                return False
        except:
            return True


class IsCompanyOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsCompanyOwner(permissions.BasePermission):
    def has_permission(self, request, view, **kwargs):
        company_name_from_url = view.kwargs.get('company', None)
        try:
            return company_name_from_url == Company.objects.get(owner=request.user).name
        except:
            return False


class UserHasCompanyOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if request.user.companies:
                return True
        except:
            return False


class IsVacancyOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return obj.company == Company.objects.get(owner=request.user)
        except:
            return False
