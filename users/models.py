from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"blank": "True", "null": "True"}


class User(AbstractUser):
    """
    Пользователь с полями почта, аватар, телефон, страна
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", **NULLABLE
    )
    phone = models.CharField(max_length=35, verbose_name="Phone", **NULLABLE)
    city = models.CharField(max_length=50, verbose_name="Country", **NULLABLE)

    token = models.CharField(max_length=100, verbose_name="Token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    CASH = "CASH"
    ONLINE = "ONLINE"
    PAYMENTS_METHOD = (
        (CASH, "Оплата наличными"),
        (ONLINE, "Перевод на счет"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE,
    )
    date = models.DateField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE
    )
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    method = models.CharField(
        max_length=50, default="Перевод на счет", choices=PAYMENTS_METHOD, verbose_name="Способ оплаты", **NULLABLE
    )

    session_id = models.CharField(
        max_length=255,
        verbose_name="ID сессии",
        **NULLABLE,
    )
    link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        **NULLABLE,
    )
    status = models.CharField(
        max_length=50,
        verbose_name="Статус платежа",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.user} - {self.course if self.course else self.lesson}"

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
        ordering = ["-date"]
