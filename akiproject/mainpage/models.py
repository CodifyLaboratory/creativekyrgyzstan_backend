from django.db import models

# Create your models here.

class MainPage(models.Model):
    short_description = models.TextField('Текст описания')
    advantages = models.TextField('Текст')

    def __str__(self):
        return "О проекте"

    class Meta:
        verbose_name = 'Преимущества и краткая информация'
        verbose_name_plural = 'Главная страница'

class Footer(models.Model):
    company_name = models.CharField('Аддрес', max_length=200, null= True, blank= True)
    company_email = models.EmailField('Почта', null= True, blank= True)
    whatsapp = models.CharField('WhatsApp', max_length=150, null= True, blank= True)
    facebook = models.URLField('Facebook', max_length=150, null= True, blank= True)
    instagram = models.URLField('instagram', max_length=150, null= True, blank= True)
    twitter = models.URLField('Twitter', max_length=150, null= True, blank= True)
    tiktok = models.URLField('TikTok', max_length=150, null= True, blank= True)
    telegram = models.URLField('Telegram', max_length=150, null= True, blank= True)

    def __str__(self):
        return "Футер"

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'