from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """
    Serializer для курса
    """

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    """
    Serializer для урока
    """

    class Meta:
        model = Lesson
        fields = "__all__"
