from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    """
    Viewset для работы с курсами.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonCreateAPIView(CreateAPIView):
    """
    API view для создания нового урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListAPIView(ListAPIView):
    """
    API view для получения списка всех уроков.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    """
    API view для получения информации о конкретном уроке.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    """
    API view для редактирования информации о уроке.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(DestroyAPIView):
    """
    API view для удаления урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
