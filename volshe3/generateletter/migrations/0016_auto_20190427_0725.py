# Generated by Django 2.1.7 on 2019-04-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0015_auto_20190427_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaletters',
            name='departure_to',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='visaletters',
            name='entry_from',
            field=models.CharField(max_length=200),
        ),
    ]
