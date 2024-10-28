from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import (CourseDetailSerializer, CourseSerializer,
                                   LessonSerializer)
from users.permissions import IsModer, IsOwner

from django.shortcuts import get_object_or_404


class CourseViewSet(ModelViewSet):
    """
    Viewset для работы с курсами.
    """
    queryset = Course.objects.all()

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
        lesson.save()


class LessonListAPIView(ListAPIView):
    """
    API view для получения списка всех уроков.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        """
        Выбирает только уроки текущего пользователя, кроме группы модератора
        """
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
