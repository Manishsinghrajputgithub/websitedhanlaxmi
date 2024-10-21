# Generated by Django 4.2.6 on 2024-08-15 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.CharField(blank=True, max_length=225, null=True)),
                ('telegram', models.CharField(blank=True, max_length=225, null=True)),
                ('support', models.CharField(blank=True, max_length=225, null=True)),
                ('upi', models.CharField(blank=True, max_length=225, null=True)),
                ('barcode', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('open', models.TimeField()),
                ('close', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='wallet',
            field=models.CharField(default=0, max_length=125),
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paytm', models.CharField(blank=True, max_length=225, null=True)),
                ('phonepay', models.CharField(blank=True, max_length=225, null=True)),
                ('gpay', models.CharField(blank=True, max_length=225, null=True)),
                ('ac', models.IntegerField(blank=True, max_length=255, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=225, null=True)),
                ('bankname', models.CharField(blank=True, max_length=255, null=True)),
                ('holder', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
