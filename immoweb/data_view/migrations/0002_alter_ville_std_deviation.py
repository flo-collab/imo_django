# Generated by Django 4.0 on 2021-12-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_view', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ville',
            name='std_deviation',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
