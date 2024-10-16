from habit.models import Habit

from rest_framework import serializers

from habit.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Реализация сериализатора для привычек."""
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator]
