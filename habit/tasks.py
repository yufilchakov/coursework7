from datetime import datetime
from celery import shared_task
from habit.models import Habit
from habit.services import send_telegram_message


@shared_task
def send_habit():
    """Отправляет Telegram-сообщения о выполнении дел в текущую дату."""
    current_date = datetime.datetime.now()
    habits = Habit.objects.filter(time=current_date)
    for habit_instance in habits:
        telegram_chat = habit_instance.user.telegram_chat_id
        message = f'Я буду {habit_instance.action} в {habit_instance.time} в {habit_instance.place}.'
        send_telegram_message(telegram_chat, message)
