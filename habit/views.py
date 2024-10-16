from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habit.models import Habit
from habit.paginators import HabitPagination
from habit.serializer import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычек."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    
    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Список привычек."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        queryset = self.queryset.filter(owner=self.request.user)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Информация о привычках."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    
    
class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    
    
class HabitPublicListAPIView(generics.ListAPIView):
    """Список публичных привычек."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = HabitPagination
