from django.db import models

NULLABLE = {"blank": "True", "null": "True"}


class Course(models.Model):
    """
    Курс.
    """

    name = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса", **NULLABLE)
    image = models.ImageField(
        upload_to="courses/", verbose_name="Изображение курса", **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]


class Lesson(models.Model):
    """
    Урок курса.
    """

    name = models.CharField(max_length=100, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока", **NULLABLE)
    image = models.ImageField(
        upload_to="lessons/", verbose_name="Изображение урока", **NULLABLE
    )
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, verbose_name="Курс", **NULLABLE
    )
    url = models.URLField(verbose_name="Ссылка на видео", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name"]
