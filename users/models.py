from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""
    username = None

    email = models.EmailField(
        unique=True, verbose_name='Почта', help_text='Укажите почту'
    )
    telephone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name='Телефон',
        help_text='Укажите номер телефона',
    )
    side = models.CharField(
        max_length=35,
        verbose_name='Страна',
        blank=True,
        null=True,
        help_text='Укажите страну',
    )
    avatar = models.ImageField(
        upload_to='users/avatars',
        blank=True,
        null=True,
        verbose_name='Аватар',
        help_text='Загрузите аватар',
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Город',
    )
    telegram_nick = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Телеграмм ник',
    )
    telegram_chat_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Телеграмм чат ID',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
