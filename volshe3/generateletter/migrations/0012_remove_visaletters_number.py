# Generated by Django 2.1.7 on 2019-04-25 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0011_visaletters_lastname_3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visaletters',
            name='Number',
        ),
    ]