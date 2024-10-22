from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    """
    Viewset для работы с курсами.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

