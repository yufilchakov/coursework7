from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.models import User
from users.serializer import UserSerializer


class UserCreateApiView(CreateAPIView):
    """Класс является представлением API для создания нового пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
