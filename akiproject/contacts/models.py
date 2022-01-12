from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField('E mail')
    telephone = models.CharField('Phone number', max_length=100)
    address = models.TextField('Address')
    telegram = models.CharField('Telegram', max_length=150)
    instagram = models.CharField('Instagram', max_length=150)
    facebook = models.CharField('Facebook', max_length=150)
    copyright = models.CharField('Copyright', max_length=200)
    studio_name = models.CharField('Studio', max_length=200)

    class Meta:
        verbose_name = 'Наш Контакт'
        verbose_name_plural = 'Наши Контакты'