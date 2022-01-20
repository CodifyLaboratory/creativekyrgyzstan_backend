from django.db import models

# Create your models here.

class RulesAndPolitics(models.Model):
    how_to = models.TextField('Как стать членом ассоциаций')
    politics = models.TextField('Устав и членская политика', null= True, blank= True)

    def __str__(self):
        return "Правила и Политика"

    class Meta:
        verbose_name = 'Устав и членская политика'
        verbose_name_plural = 'Устав и членская политика'


class Members(models.Model):
    first_name = models.CharField('Имя', max_length=70)
    last_name = models.CharField('Фамилия', max_length=70)
    middle_name = models.CharField('Отчество', max_length=70)
    photo = models.ImageField(upload_to='images/photos', null= True, blank= True)
    bio = models.TextField('Краткая биография', null= True, blank= True)

    def __str__(self):
        return (self.first_name + " " +self.last_name)

    class Meta:
        verbose_name = 'Член ассоциаций'
        verbose_name_plural = 'Члены ассоциации'