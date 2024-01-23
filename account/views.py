from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrDeny
from .models import User
from .serializers import (
    RegisterSerializer,
    UserSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrDeny, IsAuthenticated]

    def get_object(self):
        return self.request.user