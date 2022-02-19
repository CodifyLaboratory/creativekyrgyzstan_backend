from django.db import models
# Create your models here.

class Submit(models.Model):
    company_name = models.CharField('Company name', max_length=200, null= True)
    full_name = models.CharField('Full name', max_length=100, null= True)
    position = models.CharField('Position in company', max_length=100, null= True, blank= True)
    company_reg_date = models.CharField('Company registration date', max_length=50, null= True)
    company_members = models.IntegerField('Company members', null= True, blank= True)
    company_webpage = models.CharField('Company webpage', max_length=100, null= True, blank= True)
    company_socials = models.CharField('Company social pages', max_length=200, null= True, blank= True)
    company_logo = models.ImageField(upload_to='images/logo', null= True, blank= True)
    company_field = models.CharField('Company field', max_length=500, null= True)
    company_activity = models.CharField('Company activity', max_length=500, null= True)
    company_email = models.EmailField()
    company_phone = models.CharField('Company phone number', max_length=100, null= True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'