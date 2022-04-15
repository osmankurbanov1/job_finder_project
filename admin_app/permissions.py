from rest_framework import permissions


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
