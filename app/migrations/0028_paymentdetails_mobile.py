# Generated by Django 4.2.6 on 2024-09-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_admininfo_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='mobile',
            field=models.CharField(blank=True, max_length=225, null=''),
        ),
    ]