# Generated by Django 2.1.7 on 2019-04-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0003_auto_20190423_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visaletters',
            name='Date_Of_Birth_3',
        ),
        migrations.AlterField(
            model_name='visaletters',
            name='Passport_Number_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='visaletters',
            name='hotels',
            field=models.CharField(max_length=264),
        ),
    ]