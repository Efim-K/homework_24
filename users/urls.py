from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentsCreateAPIView, PaymentsListAPIView,
                         UserCreateAPIView, UserViewSet)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserViewSet)

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("payments/", PaymentsListAPIView.as_view(), name="payments_list"),
    path("payments/create/", PaymentsCreateAPIView.as_view(), name="payments_create"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]
urlpatterns += router.urls
