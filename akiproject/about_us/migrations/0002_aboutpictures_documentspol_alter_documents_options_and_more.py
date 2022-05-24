# Generated by Django 4.0.1 on 2022-04-06 16:50

import about_us.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/aboutus', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.CreateModel(
            name='DocumentsPol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('politic_doc', models.FileField(upload_to='static/document/', validators=[about_us.validators.validate_file_extension], verbose_name='Учетная политика')),
            ],
            options={
                'verbose_name': 'Учетная политика',
            },
        ),
        migrations.AlterModelOptions(
            name='documents',
            options={'verbose_name': 'Устав'},
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='mission',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='advantages',
            name='about_us',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='politic_doc',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Об Ассоциации'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Об Ассоциации'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description_kg',
            field=models.TextField(blank=True, null=True, verbose_name='Об Ассоциации'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/aboutus', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='subtitle_kg',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='text_kg',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='purpose',
            name='text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='purpose',
            name='text_kg',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='advantages',
            name='subtitle',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='advantages',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='rule_doc',
            field=models.FileField(upload_to='static/document/', validators=[about_us.validators.validate_file_extension], verbose_name='Устав'),
        ),
        migrations.AlterField(
            model_name='purpose',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='report_text',
            field=models.FileField(upload_to='static/reports/', validators=[about_us.validators.validate_file_extension], verbose_name='Отчеты'),
        ),
    ]
