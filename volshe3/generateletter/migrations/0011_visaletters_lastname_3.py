# Generated by Django 2.2 on 2019-04-24 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0010_visaletters_no_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='visaletters',
            name='lastname_3',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
