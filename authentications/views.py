from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserSerializer, TokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = TokenSerializer


class UserList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.exclude(pk=self.request.user.pk)
    