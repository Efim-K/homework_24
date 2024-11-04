from rest_framework.validators import ValidationError


def url_validator(value):
    """
    Валидатор для проверки ссылки на видео
    """
    if not value:
        return None
    elif 'youtube.com' not in value:
        raise ValidationError("Ссылка на видео разрешена только с сайта youtube.com")
