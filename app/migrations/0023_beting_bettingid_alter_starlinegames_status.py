# Generated by Django 4.2.6 on 2024-09-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_galidesawargame_holiday_games_holiday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='beting',
            name='bettingid',
            field=models.CharField(blank=True, max_length=225, null=''),
        ),
        migrations.AlterField(
            model_name='starlinegames',
            name='status',
            field=models.CharField(blank=True, default='close', max_length=225, null=''),
        ),
    ]
