from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField('Название статьи', max_length=400)
    text = models.TextField('Текст татьи')
    image = models.ImageField(upload_to='images/', null= True, blank= True)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'