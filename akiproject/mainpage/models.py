from django.db import models

# Create your models here.

class MainPage(models.Model):
    short_description = models.TextField('Текст описания')
    advantages = models.TextField('Текст')

    def __str__(self):
        return "О проекте"

    class Meta:
        verbose_name = 'Преймущества и краткая информация'
        verbose_name_plural = 'Главная страница'