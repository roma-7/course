from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'PUT', 'DELETE']:
            return True
        return obj.created_by == request.user


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_authenticated


class IsStudentOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user and obj.course.is_completed


class  CheckCartItem(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user and obj.course.is_completed
