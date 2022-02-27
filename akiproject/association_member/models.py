from django.db import models
# from akiproject.about_us.models import Supervisory
from submit.models import Submit

class RulesAndPolitics(models.Model):
    how_to = models.TextField('Как стать членом ассоциаций')
    politics = models.TextField('Устав и членская политика', null= True, blank= True)

    def __str__(self):
        return "Правила и Политика"

    class Meta:
        verbose_name = 'Устав и членская политика'
        verbose_name_plural = 'Устав и членская политика'


class Members(models.Model):
    submit = models.OneToOneField(Submit, verbose_name='Выберите из ЗАЯВКИ или уже выбран чтобы посмотреть нажмите на карандаш', on_delete=models.SET_NULL, null=True, related_name='submit')
    photo = models.ImageField('Фото руководителя', upload_to='images/members', null= True, blank= True)
    bio = models.TextField('Краткая биография', null= True, blank= True)


    def __str__(self):
        return f'{self.submit.full_name}'

    class Meta:
        verbose_name = 'Члены ассоциаций'
        verbose_name_plural = 'Члены ассоциации'