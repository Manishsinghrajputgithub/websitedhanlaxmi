# Generated by Django 4.2.6 on 2024-08-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_admininfo_games_customer_wallet_paymentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]