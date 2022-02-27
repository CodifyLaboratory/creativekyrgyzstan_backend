# Generated by Django 4.0.1 on 2022-02-27 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('association_member', '0003_alter_members_photo'),
        ('about_us', '0003_alter_reports_report_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisory',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='supervisory',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='supervisory',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='supervisory',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='supervisory',
            name='member',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member', to='association_member.members'),
        ),
        migrations.AlterField(
            model_name='supervisory',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/photos', verbose_name='Фото руководителя'),
        ),
    ]