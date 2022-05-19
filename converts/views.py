from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from converts.models import Convert
from converts.serializers import ConvertSerializer, ClearSerializer
from converts.permissions import ConvertPermissions, ClearPermissions


class ConvertViewSet(viewsets.ModelViewSet):
    serializer_class = ConvertSerializer
    queryset = Convert.objects.all()
    permission_classes = [ConvertPermissions]
    
    def list(self, request, *args, **kwargs):
        converts = Convert.objects.filter(user_id=self.request.user.id)
        serializer = ConvertSerializer(converts, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        get_object_or_404(Convert, id = self.kwargs['pk']).delete()
        return Response({'message': f"La conversion {self.kwargs['pk']} est effacée"})

class ClearViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = ClearSerializer
    queryset = Convert.objects.all()
    permission_classes = [ClearPermissions]
    
    def list(self, request, *args, **kwargs):
        user_connected = request.user.id
        Convert.objects.filter(user_id=user_connected).delete()
        return Response({'message': f"L'historique de l'utilisateur {user_connected} est effacé"})
    

