from django.db import models

class AboutUs(models.Model):
    short_description = models.TextField('Об Ассоциации')
    mission = models.TextField('Миссия и ценности')
    

    class Meta:
        verbose_name = 'Об Ассоциации'
        verbose_name_plural = 'Об Ассоциации'


    def __str__(self) -> str:
        return 'О нас '

class Supervisory(models.Model):  #наблюдательный совет
    first_name = models.CharField('Имя', max_length=70)
    last_name = models.CharField('Фамилия', max_length=70)
    middle_name = models.CharField('Отчество', max_length=70, null=True, blank=True)
    company_name = models.CharField('Названии компании', max_length=300, blank=True, null=True)
    photo = models.ImageField(upload_to='images/photos', null= True, blank= True)
    add_info = models.TextField('Дополнительная информация')
    

    class Meta:
        verbose_name = 'Член наблюдательного совета'
        verbose_name_plural = 'Члены наблюдательного совета'



    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}, {self.company_name}'



from .validators import validate_file_extension

class Reports(models.Model):
    name = models.TextField('Название отчета')
    short_description = models.TextField('Краткое описание', blank=True, null=True)
    report_text = models.FileField('Отчеты', upload_to='static/reports/name/%d/%m/%Y', validators=[validate_file_extension])
    created_date = models.DateField('Дата создания', blank=True, null=True)
    signature = models.TextField('Должность Ф.И.О. подпись', blank=True, null=True)
    add_info = models.TextField('Дополнительная информация', blank=True, null=True)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'


    def __str__(self) -> str:
        return f'{self.name}, Дата создания: {self.created_date}'
    

