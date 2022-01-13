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

class Reports(models.Model):
    name = models.TextField('Название отчета')
    short_description = models.TextField('Краткое описание', blank=True, null=True)
    report_text = models.TextField('Отчет')
    created_date = models.DateField('Дата создания', blank=True, null=True)
    signature = models.TextField('Должность Ф.И.О. подпись', blank=True, null=True)
    add_info = models.TextField('Дополнительная информация', blank=True, null=True)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'


    def __str__(self) -> str:
        return f'{self.name}, Дата создания: {self.created_date}'
    
        # Добавление, удаление информации о членах наблюдательного совета и отчетов 


#          О нас
# Об Ассоциации
# Миссия и ценности 
# Инфо наблюдательном совете и членах наблюдательного совета 
# Отчеты 



# Краткая информация об АКИ
# Визуально отдельный  блок с текстом о миссии и ценностях АКИ
# Перечень членов наблюдательного совета- фото, ФИО, название компании.   https://goo.su/9ub6 (члены НС АКИ)
# Раздел для  загрузки отчетов АКИ, с возможность давать название отчету и загрузки на сайт в виде приложения 
# для скачивания или просмотра на отдельной странице. Отчетов может быть неопределенное кол-во. 


