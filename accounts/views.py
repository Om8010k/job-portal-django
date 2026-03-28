from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import RegisterSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# ================= REGISTER =================
class RegisterView(generics.CreateAPIView):
    """
    Register new user
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            "message": "User registered successfully",
            "data": response.data
        }, status=status.HTTP_201_CREATED)


# ================= LOGIN =================
class CustomTokenSerializer(TokenObtainPairSerializer):
    """
    Add user role in JWT response
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        data["role"] = self.user.role
        return data


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer