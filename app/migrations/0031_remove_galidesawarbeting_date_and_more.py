# Generated by Django 4.2.6 on 2024-09-24 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_remove_starlinegames_result_starlinegames_jodi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galidesawarbeting',
            name='date',
        ),
        migrations.RemoveField(
            model_name='starlinebeting',
            name='date',
        ),
        migrations.AlterField(
            model_name='galidesawarbeting',
            name='join',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='starlinebeting',
            name='join',
            field=models.DateField(blank=True),
        ),
    ]
