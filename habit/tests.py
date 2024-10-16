from rest_framework import status

from rest_framework.test import APITestCase
from django.urls import reverse

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование привычек."""
    def setUp(self):
        self.user = User.objects.create(email='admin@example.com', password='123qwe')
        self.habit = Habit.objects.create(place='Спорт зал', owner=self.user, time='12:30:00')
        self.client.force_authenticate(user=self.user)
    
    def test_habit_retrieve(self):
        url = reverse('habit:habit_retrieve', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('place'), self.habit.place)
    
    def test_habit_create(self):
        url = reverse('habit:habit_create')
        data = {
            'place': 'Домашние дела',
            'time': '14:00:00',
            'action': 'Убирать пыль',
            'owner': self.user.pk,
        }
        self.client.force_login(self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Habit.objects.get(place="Домашние дела", time='14:00:00', action='Убирать пыль').owner, self.user
        )
    
    def test_habit_update(self):
        url = reverse('habit:habit_update', args=(self.habit.pk,))
        data = {
            'place': 'Учебный зал',
            'time': '16:00:00',
            'action': 'Продолжать изучать',
            'owner': self.user.pk,
        }
        self.client.force_login(self.user)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Habit.objects.get(pk=self.habit.pk).place, 'Учебный зал'
        )
    
    def test_habit_delete(self):
        url = reverse('habit:habit_delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.filter(pk=self.habit.pk).exists(), False)
    
    def test_habit_list(self):
        url = reverse('habit:habit_list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': self.habit.pk,
                    'place': self.habit.place,
                    'time': self.habit.time,
                    'action': self.habit.action,
                    'pleasant_habit': False,
                    'periodicity': 1,
                    'reward': None,
                    'time_to_complete': 120,
                    'publicity': False,
                    'is_public': True,
                    'owner': 3,
                    'linked_habit': None
                }
            ],
        }
        self.assertEqual(data, result)
    
    def test_public_list(self):
        url = reverse('habit:public_list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('count'), 1)
