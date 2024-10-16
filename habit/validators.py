from rest_framework import serializers


class HabitValidator:
    """Валидатор для привычек."""
    def __init__(self, instance):
        self.instance = instance

    def __call__(self, field, value):
        if field == 'linked_habit':
            if value and self.instance.reward:
                raise serializers.ValidationError('Нельзя одновременно указать связанную привычку и вознаграждение')
            if value and not self.instance.pleasant_habit:
                raise serializers.ValidationError('Связанная привычка должна быть приятной привычкой')
        elif field == 'reward':
            if self.instance.pleasant_habit and value:
                raise serializers.ValidationError('Приятные привычки не могут иметь вознаграждений')
        elif field == 'time_to_complete':
            if value > 120:
                raise serializers.ValidationError('Время выполнения не должно быть больше 120 секунд')
        elif field == 'periodicity':
            if value < 1 or value > 7:
                raise serializers.ValidationError('Периодичность привычки не должна быть меньше 1 раза в 7 дней')
