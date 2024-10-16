from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания администратора с правами суперпользователя."""
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@example.com")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("123qwe")
        user.save()
