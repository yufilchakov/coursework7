from django.db import models

from config.settings import AUTH_USER_MODEL


class Habit(models.Model):
    """Модель привычка."""
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    place = models.CharField(
        max_length=100,
        verbose_name='Место'
    )
    time = models.TimeField(
        max_length=15,
        verbose_name='Время, когда необходимо выполнять привычку'
    )
    action = models.CharField(
        max_length=100,
        verbose_name='Действие, которое представляет собой привычка'
    )
    pleasant_habit = models.BooleanField(
        default=False,
        verbose_name='Является ли привычка приятной'
    )
    linked_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Связанная привычка'
    )
    periodicity = models.IntegerField(
        default=1,
        verbose_name='Периодичность'
    )
    reward = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Вознаграждение'
    )
    time_to_complete = models.IntegerField(
        default=120,
        verbose_name='Время на выполнение'
    )
    publicity = models.BooleanField(
        default=False,
        verbose_name='Признак публичности'
    )
    is_public = models.BooleanField(
        default=True,
        verbose_name='Публичная'
    )
    
    def __str__(self):
        return f'я буду {self.action} в {self.time} в {self.place}'
    
    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
