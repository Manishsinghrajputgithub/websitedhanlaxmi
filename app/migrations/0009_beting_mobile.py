# Generated by Django 4.2.6 on 2024-08-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_result_games_closepanna_games_jodipanna_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='beting',
            name='mobile',
            field=models.CharField(blank=True, max_length=225, null=''),
        ),
    ]
