# Generated by Django 4.0.1 on 2022-03-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreativeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Название статьи')),
                ('text', models.TextField(verbose_name='Текст татьи')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/CreativeProjects', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Креативный проект',
                'verbose_name_plural': 'Креативные проекты',
            },
        ),
        migrations.CreateModel(
            name='FormalRegistrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Название статьи')),
                ('text', models.TextField(verbose_name='Текст татьи')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/FormalRegistrations', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Название статьи')),
                ('text', models.TextField(verbose_name='Текст татьи')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/recommendtaions', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Рекомендация',
                'verbose_name_plural': 'Рекомендаций',
            },
        ),
    ]
