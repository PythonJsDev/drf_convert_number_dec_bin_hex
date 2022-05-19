from django.shortcuts import get_object_or_404
from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()

class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user_id = view.kwargs.get('pk')
        if request.user.is_admin:
            return True
        if request.method == 'GET':
            if user_id:    
                if str(request.user.id) == user_id:
                    return True
           
            
            
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.id:
            return True
        
