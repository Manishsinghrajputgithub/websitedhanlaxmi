# Generated by Django 4.2.6 on 2024-09-13 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_beting_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beting',
            name='join',
            field=models.DateTimeField(blank=True),
        ),
    ]
