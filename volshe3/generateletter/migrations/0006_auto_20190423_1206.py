# Generated by Django 2.1.7 on 2019-04-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0005_auto_20190423_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='visaletters',
            name='Date_Of_Birth_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='visaletters',
            name='Date_Of_Birth_3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='visaletters',
            name='Date_Of_Birth_4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='visaletters',
            name='Date_of_letter',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
