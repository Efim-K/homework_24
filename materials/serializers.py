from rest_framework.serializers import ModelSerializer

from materials.models import Course


class CourseSerializer(ModelSerializer):
    """
    Serializer для курса
    """

    class Meta:
        model = Course
        fields = '__all__'
