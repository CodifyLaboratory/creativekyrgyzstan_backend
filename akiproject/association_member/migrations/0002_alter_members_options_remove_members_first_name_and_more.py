# Generated by Django 4.0.1 on 2022-02-27 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0003_remove_submit_company_socials_submit_facebook_and_more'),
        ('association_member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name': 'Члены ассоциаций', 'verbose_name_plural': 'Члены ассоциации'},
        ),
        migrations.RemoveField(
            model_name='members',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='members',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='members',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='members',
            name='submit',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submit', to='submit.submit'),
        ),
        migrations.AlterField(
            model_name='members',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/members'),
        ),
    ]
