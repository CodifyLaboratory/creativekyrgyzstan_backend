# Generated by Django 4.0.1 on 2022-04-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_alter_recommendation_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст статьи'),
        ),
    ]
