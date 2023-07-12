from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField('Название статьи', max_length=400)
    text = models.TextField('Текст татьи')
    name_kg = models.CharField('Название статьи_kg', max_length=400, null=True, blank=True)
    text_kg = models.TextField('Текст татьи_kg', null=True, blank=True)
    name_en = models.CharField('Название статьи_en', max_length=400, null=True, blank=True)
    text_en = models.TextField('Текст татьи_en', null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField('Дата проведения', auto_now_add=False)
    draft = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

class EventImages(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null= True, blank= True)

    def __str__(self) -> str:
        return (str(self.event))

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'