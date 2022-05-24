# Generated by Django 4.0.1 on 2022-03-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, null=True, verbose_name='Полное наименование')),
                ('full_name', models.CharField(max_length=100, null=True, verbose_name='ФИО руководителя')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность руководителя')),
                ('company_reg_date', models.DateField(max_length=50, null=True, verbose_name='Дата регистрации компании/ИП ')),
                ('company_members', models.IntegerField(blank=True, null=True, verbose_name='Количество сотрудников')),
                ('company_webpage', models.URLField(blank=True, max_length=100, null=True, verbose_name='Сайт компании/ИП')),
                ('facebook', models.CharField(blank=True, max_length=150, null=True, verbose_name='Facebook')),
                ('telegram', models.CharField(blank=True, max_length=150, null=True, verbose_name='Telegram')),
                ('whatsapp', models.CharField(blank=True, max_length=150, null=True, verbose_name='WhatsApp')),
                ('instagram', models.CharField(blank=True, max_length=150, null=True, verbose_name='instagram')),
                ('twitter', models.CharField(blank=True, max_length=150, null=True, verbose_name='Twitter')),
                ('tiktok', models.CharField(blank=True, max_length=150, null=True, verbose_name='TikTok')),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='images/logo', verbose_name='Логотип')),
                ('company_field', models.CharField(max_length=500, null=True, verbose_name='Креативная отрасль компании')),
                ('company_activity', models.CharField(max_length=500, null=True, verbose_name='Деятельность компании')),
                ('company_email', models.EmailField(max_length=254, null=True, verbose_name='Почта')),
                ('company_phone', models.CharField(max_length=100, null=True, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
