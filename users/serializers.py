from rest_framework.serializers import ModelSerializer

from users.models import Payments, User


class PaymentsSerializer(ModelSerializer):
    """
    Serializer для платежей
    """

    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """
    Serializer для пользователя
    """

    # Отображаем платежи пользователя
    payments = PaymentsSerializer(source="payments_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
