from rest_framework import permissions
from company_app.models import Company


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
        return obj.company == Company.objects.get(owner=request.user)
