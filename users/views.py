from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    """
    API view для получения списка всех пользователей.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsListAPIView(ListAPIView):
    """
    API view для получения списка всех платежей.
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = (
        "course",
        "lesson",
    )
    ordering_fields = ("date",)
    search_fields = ("method",)


class PaymentsCreateAPIView(CreateAPIView):
    """
    API view для создания нового платежа.
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

