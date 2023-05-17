from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.users.api.serializers import UserSerializer
from utils.permissions import IsOwnerOrAdmin

User = get_user_model()


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsOwnerOrAdmin()]
        return [AllowAny()]
