# Generated by Django 4.0.1 on 2022-03-02 15:26

import about_us.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('association_member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.TextField(verbose_name='Об Ассоциации')),
                ('mission', models.TextField(verbose_name='Миссия и ценности')),
            ],
            options={
                'verbose_name': 'Об Ассоциации',
                'verbose_name_plural': 'Об Ассоциации',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_doc', models.FileField(upload_to='static/document/%d/%m/%Y', validators=[about_us.validators.validate_file_extension], verbose_name='Устав')),
                ('politic_doc', models.FileField(upload_to='static/document/%d/%m/%Y', validators=[about_us.validators.validate_file_extension], verbose_name='Учетная политика')),
            ],
            options={
                'verbose_name': 'Устав, Учетная политика',
            },
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Цели на год',
                'verbose_name_plural': 'Цели на год',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название отчета')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('report_text', models.FileField(upload_to='static/reports/%d/%m/%Y', validators=[about_us.validators.validate_file_extension], verbose_name='Отчеты')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('signature', models.TextField(blank=True, null=True, verbose_name='Должность Ф.И.О. подпись')),
                ('add_info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
        migrations.CreateModel(
            name='Supervisory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/photos', verbose_name='Фото руководителя')),
                ('add_info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('member', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='association_member.members', verbose_name='Выберите из Члены  АКИ или уже выбран чтобы посмотреть нажмите на карандаш')),
            ],
            options={
                'verbose_name': 'Член наблюдательного совета',
                'verbose_name_plural': 'Члены наблюдательного совета',
            },
        ),
        migrations.CreateModel(
            name='Founders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/photos', verbose_name='Фото руководителя')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('founder', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='association_member.members', verbose_name='Выберите из Члены  АКИ или уже выбран чтобы посмотреть нажмите на карандаш')),
            ],
            options={
                'verbose_name': 'Учредители Ассоциации',
                'verbose_name_plural': 'Учредители Ассоциации',
            },
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Заголовка')),
                ('text', models.TextField(verbose_name='Текст')),
                ('about_us', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about_us.aboutus')),
            ],
            options={
                'verbose_name': 'Почему ценно быть членов АКИ',
                'verbose_name_plural': 'Почему ценно быть членов АКИ',
            },
        ),
    ]
