# Generated by Django 4.2.6 on 2024-09-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_beting'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=225, null='')),
                ('amount', models.IntegerField(blank=True, max_length=225, null='')),
                ('utr', models.CharField(blank=True, max_length=225, null='')),
                ('status', models.CharField(blank=True, max_length=225, null='')),
                ('join', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]