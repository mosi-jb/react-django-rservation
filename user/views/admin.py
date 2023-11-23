from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets

from user.models import User
from user.serializers.admin import AdminLoginSerializer, UserSerializer


class AdminLoginView(ObtainAuthToken):
    serializer_class = AdminLoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
