# Generated by Django 4.0.1 on 2022-02-27 13:04

import about_us.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_alter_reports_report_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='report_text',
            field=models.FileField(upload_to='static/reports/%d/%m/%Y', validators=[about_us.validators.validate_file_extension], verbose_name='Отчеты'),
        ),
    ]