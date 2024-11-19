from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.paginators import ViewPagination
from materials.serializers import (CourseDetailSerializer, CourseSerializer,
                                   LessonSerializer, SubscriptionSerializer)
from users.permissions import IsModer, IsOwner

from rest_framework.generics import get_object_or_404

from materials.tasks import add


class CourseViewSet(ModelViewSet):
    """
    Viewset для работы с курсами.
    """
    queryset = Course.objects.all()
    pagination_class = ViewPagination

    def get_serializer_class(self):
        """
        В зависимости от действия возвращает соответствующий serializer.
        """
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        """
        Привязывает создаваемый курс текущим пользователем.
        """
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """
        Проверяет права доступа для различных действий.
        """
        if self.action in ['create', ]:
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner | ~IsModer,)
        return super().get_permissions()

    def get_queryset(self):
        """
        Выбирает только курсы текущего пользователя, кроме группы модератора
        """
        if (self.permission_classes != (IsModer | IsOwner,)):
            return Course.objects.none()

        if self.request.user.groups.filter(name="moders").exists():
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)


class LessonCreateAPIView(CreateAPIView):
    """
    API view для создания нового урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModer)

    def perform_create(self, serializer):
        """
        Привязывает создаваемый урок текущим пользователем.
        """
        lesson = serializer.save()
        lesson.owner = self.request.user
        add.delay()
        lesson.save()


class LessonListAPIView(ListAPIView):
    """
    API view для получения списка всех уроков.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = ViewPagination

    def get_queryset(self):
        """
        Выбирает только уроки текущего пользователя, кроме группы модератора
        """
        if (self.permission_classes != (IsModer | IsOwner,)):
            return Lesson.objects.none()

        if self.request.user.groups.filter(name="moders").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonDetailAPIView(RetrieveAPIView):
    """
    API view для получения информации о конкретном уроке.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonRetrieveAPIView(RetrieveAPIView):
    """
    API view для получения информации о конкретном уроке.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonUpdateAPIView(UpdateAPIView):
    """
    API view для редактирования информации о уроке.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonDestroyAPIView(DestroyAPIView):
    """
    API view для удаления урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModer | IsOwner)


class SubscriptionViewSet(APIView):
    """
    API эндпоинт для создания подписки на курс
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, request):
        """
        Создание или удаление подписки на курс
        """
        user_id = request.user
        course_id = request.data.get('course_id')
        course_item = get_object_or_404(Course, id=course_id)
        sub_item = Subscription.objects.filter(user=user_id, course=course_item)

        if sub_item.exists():
            sub_item.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=user_id, course=course_item)
            message = "Подписка добавлена"
        return Response({"message": message})
