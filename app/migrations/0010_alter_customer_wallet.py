# Generated by Django 4.2.6 on 2024-08-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_beting_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='wallet',
            field=models.IntegerField(default=0, max_length=125),
        ),
    ]