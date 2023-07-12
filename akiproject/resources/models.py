from django.db import models

# Create your models here.

class HeaderText(models.Model):
    text = models.TextField('Заглавный текст', null=True, blank=True)
    text_kg = models.TextField('Заглавный текст_kg', null=True, blank=True)
    text_en = models.TextField('Заглавный текст_en', null=True, blank=True)
    

class Recommendation(models.Model):
    name = models.CharField('Название статьи', max_length=400,  null=True, blank=True)
    description = models.TextField('Текст описания',  null=True, blank=True)
    text = models.TextField('Текст статьи', null=True, blank=True)
    name_kg = models.CharField('Название статьи_kg', max_length=400,  null=True, blank=True)
    description_kg = models.TextField('Текст описания_kg',  null=True, blank=True)
    text_kg = models.TextField('Текст статьи_kg',  null=True, blank=True)
    name_en = models.CharField('Название статьи_en', max_length=400, null=True, blank=True)
    description_en = models.TextField('Текст описания_en',  null=True, blank=True)
    text_en = models.TextField('Текст статьи_en',  null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('Изображение', upload_to='images/recommendtaions', null= True, blank= True)

    class Meta:
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендаций'
    
    def __str__(self) -> str:
        return (str(self.name))

class CreativeProject(models.Model):
    name = models.CharField('Название статьи', max_length=400,  null=True, blank=True)
    description = models.TextField('Текст описания',  null=True, blank=True)
    text = models.TextField('Текст статьи', null=True, blank=True)
    name_kg = models.CharField('Название статьи_kg', max_length=400,  null=True, blank=True)
    description_kg = models.TextField('Текст описания_kg',  null=True, blank=True)
    text_kg = models.TextField('Текст статьи_kg',  null=True, blank=True)
    name_en = models.CharField('Название статьи_en', max_length=400, null=True, blank=True)
    description_en = models.TextField('Текст описания_en',  null=True, blank=True)
    text_en = models.TextField('Текст статьи_en',  null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('Изображение', upload_to='images/CreativeProjects', null= True, blank= True)

    class Meta:
        verbose_name = 'Креативный проект'
        verbose_name_plural = 'Креативные проекты'

    def __str__(self) -> str:
        return (str(self.name))

class FormalRegistrations(models.Model):
    name = models.CharField('Название статьи', max_length=400,  null=True, blank=True)
    description = models.TextField('Текст описания',  null=True, blank=True)
    text = models.TextField('Текст статьи', null=True, blank=True)
    name_kg = models.CharField('Название статьи_kg', max_length=400,  null=True, blank=True)
    description_kg = models.TextField('Текст описания_kg',  null=True, blank=True)
    text_kg = models.TextField('Текст статьи_kg',  null=True, blank=True)
    name_en = models.CharField('Название статьи_en', max_length=400, null=True, blank=True)
    description_en = models.TextField('Текст описания_en',  null=True, blank=True)
    text_en = models.TextField('Текст статьи_en',  null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('Изображение', upload_to='images/FormalRegistrations', null= True, blank= True)

    def __str__(self) -> str:
        return (str(self.name))