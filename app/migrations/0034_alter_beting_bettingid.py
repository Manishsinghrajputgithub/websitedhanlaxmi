# Generated by Django 4.2.6 on 2024-09-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_beting_winamount_galidesawarbeting_winamount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beting',
            name='bettingid',
            field=models.CharField(blank=True, default='0', max_length=225),
        ),
    ]