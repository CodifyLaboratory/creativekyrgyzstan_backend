from email.mime import image
from django.db import models
from association_member.models import Members
from submit.models import Submit


class AboutPictures(models.Model):
    picture = models.ImageField('Картинка', upload_to='images/aboutus', null= True, blank= True) 

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self) -> str:
        return (str(self.picture))

class AboutUs(models.Model):
    description = models.TextField('Об Ассоциации', null=True, blank=True)
    description_kg = models.TextField('Об Ассоциации_kg', null=True, blank=True)
    description_en = models.TextField('Об Ассоциации_en', null=True, blank=True)
    picture = models.ImageField('Картинка', upload_to='images/aboutus', null= True, blank= True) 

    class Meta:
        verbose_name = 'Об Ассоциации'
        verbose_name_plural = 'Об Ассоциации'

    def __str__(self) -> str:
        return (str(self.description))


class Advantages(models.Model):
    subtitle = models.CharField('Заголовок', max_length=300, null=True, blank=True)
    text = models.TextField('Текст', null=True, blank=True)
    subtitle_kg = models.CharField('Заголовок_kg', max_length=300, null=True, blank=True)
    text_kg = models.TextField('Текст_kg', null=True, blank=True)
    subtitle_en = models.CharField('Заголовок_en', max_length=300, null=True, blank=True)
    text_en = models.TextField('Текст_en', null=True, blank=True)

    class Meta:
        verbose_name = 'Почему ценно быть членов АКИ'
        verbose_name_plural = 'Почему ценно быть членов АКИ'



class Purpose(models.Model):
    text = models.TextField('Текст', null=True, blank=True)
    text_kg = models.TextField('Текст_kg', null=True, blank=True)
    text_en = models.TextField('Tекст_en', null=True, blank=True)

    class Meta:
        verbose_name = 'Цели на год'
        verbose_name_plural = 'Цели на год'  


    def __str__(self) -> str:
        return 'Цели на год'


class Founders(models.Model): 
    founder = models.OneToOneField(Submit, verbose_name='Выберите из Члены  АКИ или уже выбран чтобы посмотреть нажмите на карандаш', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField('Фото руководителя', upload_to='images/photos', null= True, blank= True)
    info = models.TextField('Дополнительная информация', null=True, blank=True)   

    class Meta:
        verbose_name = 'Учредители Ассоциации'
        verbose_name_plural = 'Учредители Ассоциации'

    def __str__(self) -> str:
        return (str(self.founder))



class Supervisory(models.Model):  #наблюдательный совет
    member = models.OneToOneField(Members, verbose_name='Выберите из Члены  АКИ или уже выбран чтобы посмотреть нажмите на карандаш', on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField('Фото руководителя', upload_to='images/photos', null= True, blank= True)
    add_info = models.TextField('Дополнительная информация', null=True, blank=True)   

    class Meta:
        verbose_name = 'Член наблюдательного совета'
        verbose_name_plural = 'Члены наблюдательного совета'


    def __str__(self) -> str:
        return (str(self.member))


from .validators import validate_file_extension

class Reports(models.Model):
    name = models.TextField('Название отчета', blank=True, null=True)
    short_description = models.TextField('Краткое описание', blank=True, null=True)
    name_kg = models.TextField('Название отчета_kg', blank=True, null=True)
    short_description_kg = models.TextField('Краткое описание_kg', blank=True, null=True)
    name_en = models.TextField('Название отчета_en', blank=True, null=True)
    short_description_en = models.TextField('Краткое описание_en', blank=True, null=True)
    report_text = models.FileField('Отчеты', upload_to='static/reports/', validators=[validate_file_extension])
    created_date = models.DateField('Дата создания', blank=True, null=True)
    signature = models.TextField('Должность Ф.И.О. подпись', blank=True, null=True)
    add_info = models.TextField('Дополнительная информация', blank=True, null=True)
    add_info_kg = models.TextField('Дополнительная информация_kg', blank=True, null=True)
    add_info_en = models.TextField('Дополнительная информация_en', blank=True, null=True)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'


    def __str__(self) -> str:
        return f'{self.name}, Дата создания: {self.created_date}'


class Documents(models.Model):
    name = models.CharField('Название документа', max_length=500, null=True, blank=True)
    name_kg = models.CharField('Название документа_kg', max_length=500, null=True, blank=True)
    name_en = models.CharField('Название документа_en', max_length=500, null=True, blank=True)  
    rule_doc = models.FileField('Устав', upload_to='static/document/', validators=[validate_file_extension])              

    class Meta:
        verbose_name = 'Устав'

    def __str__(self) -> str:
        return f'{self.name}' 

class DocumentsPol(models.Model):
    name = models.CharField('Название документа', max_length=500, null=True, blank=True)
    name_kg = models.CharField('Название документа_kg', max_length=500, null=True, blank=True)
    name_en = models.CharField('Название документа_en', max_length=500, null=True, blank=True)            
    politic_doc = models.FileField('Учетная политика', upload_to='static/document/', validators=[validate_file_extension])   

    class Meta:
        verbose_name = 'Учетная политика'

    def __str__(self) -> str:
        return f'{self.name}'        
    
    

