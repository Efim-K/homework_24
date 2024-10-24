from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """
    Serializer для урока
    """

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    """
    Serializer для курса
    """

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    """
    Serializer для детального представления курса
    """
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, instance):
        """
        Возвращает количество уроков в курсе
        """
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ('name', 'description', 'count_lessons')
