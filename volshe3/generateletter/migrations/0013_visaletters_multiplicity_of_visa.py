# Generated by Django 2.1.7 on 2019-04-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0012_remove_visaletters_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='visaletters',
            name='Multiplicity_of_visa',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=264),
        ),
    ]
