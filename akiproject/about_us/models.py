from email.mime import image
from django.db import models
from association_member.models import Members
from submit.models import Submit


class AboutUs(models.Model):
    short_description = models.TextField('Об Ассоциации')
    mission = models.TextField('Миссия и ценности')
    

    class Meta:
        verbose_name = 'Об Ассоциации'
        verbose_name_plural = 'Об Ассоциации'


    def __str__(self) -> str:
        return 'О нас '



class Founders(models.Model): 
    founder = models.OneToOneField(Members, verbose_name='Выберите из Члены  АКИ или уже выбран чтобы посмотреть нажмите на карандаш', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField('Фото руководителя', upload_to='images/photos', null= True, blank= True)
    info = models.TextField('Дополнительная информация', null=True, blank=True)   

    class Meta:
        verbose_name = 'Учредители Ассоциации'
        verbose_name_plural = 'Учредители Ассоциации'



    def __str__(self) -> str:
        return f'{self.founder.submit.full_name}, {self.founder.submit.company_name}'



class Supervisory(models.Model):  #наблюдательный совет
    member = models.OneToOneField(Members, verbose_name='Выберите из Члены  АКИ или уже выбран чтобы посмотреть нажмите на карандаш', on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField('Фото руководителя', upload_to='images/photos', null= True, blank= True)
    add_info = models.TextField('Дополнительная информация', null=True, blank=True)   

    class Meta:
        verbose_name = 'Член наблюдательного совета'
        verbose_name_plural = 'Члены наблюдательного совета'



    def __str__(self) -> str:
        return f'{self.member.submit.full_name}, {self.member.submit.company_name}'



from .validators import validate_file_extension

class Reports(models.Model):
    name = models.TextField('Название отчета')
    short_description = models.TextField('Краткое описание', blank=True, null=True)
    report_text = models.FileField('Отчеты', upload_to='static/reports/%d/%m/%Y', validators=[validate_file_extension])
    created_date = models.DateField('Дата создания', blank=True, null=True)
    signature = models.TextField('Должность Ф.И.О. подпись', blank=True, null=True)
    add_info = models.TextField('Дополнительная информация', blank=True, null=True)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'


    def __str__(self) -> str:
        return f'{self.name}, Дата создания: {self.created_date}'
    

