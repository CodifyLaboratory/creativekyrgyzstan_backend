from django.db import models

# from association_member.models import Members
# Create your models here.

class Submit(models.Model):
    company_name = models.CharField('Полное наименование', max_length=200, null= True)
    full_name = models.CharField('ФИО руководителя', max_length=100, null= True)
    position = models.CharField('Должность руководителя', max_length=100, null= True, blank= True)
    # company_reg_date = models.DateField('Дата регистрации компании/ИП ', max_length=50, null= True)
    # company_members = models.IntegerField('Количество сотрудников', null= True, blank= True)
    # company_webpage = models.URLField('Сайт компании/ИП', max_length=100, null= True, blank= True)
    facebook = models.URLField('Facebook', max_length=150, null= True, blank= True)
    telegram = models.URLField('Telegram', max_length=150, null= True, blank= True)
    # whatsapp = models.CharField('WhatsApp', max_length=150, null= True, blank= True)
    instagram = models.URLField('instagram', max_length=150, null= True, blank= True)
    twitter = models.URLField('Twitter', max_length=150, null= True, blank= True)
    # tiktok = models.URLField('TikTok', max_length=150, null= True, blank= True)
    company_logo = models.ImageField('Логотип', upload_to='images/logo', null= True, blank= True)
    company_field = models.CharField('Креативная отрасль компании', max_length=500, null= True, blank= True)
    company_activity = models.CharField('Деятельность компании', max_length=500, null= True, blank= True)
    company_email = models.EmailField('Почта', null= True, blank= True)
    company_phone = models.CharField('Телефон', max_length=100, null= True, blank= True)



    def __str__(self):
        return f'{self.company_name}, {self.full_name}'
        
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'