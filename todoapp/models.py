from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField("Названия задания", max_length=500)
    is_complete = models.BooleanField("Заверщено", default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title
