# Generated by Django 3.0.8 on 2020-07-29 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
    ]
