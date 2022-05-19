
from django.shortcuts import get_object_or_404
from rest_framework import permissions

from converts.models import Convert


class ConvertPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        convert = get_object_or_404(Convert, id=obj.id)
        if request.user.id == convert.user_id:
            return True


class ClearPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':        
            return True
    
