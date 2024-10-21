# Generated by Django 4.2.6 on 2024-09-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_delete_beting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=225, null='')),
                ('name', models.CharField(blank=True, max_length=225, null='')),
                ('pana_name', models.CharField(blank=True, max_length=225, null='')),
                ('digit', models.CharField(blank=True, max_length=225, null='')),
                ('points', models.CharField(blank=True, max_length=225, null='')),
                ('gametype', models.CharField(blank=True, max_length=225, null='')),
                ('status', models.CharField(blank=True, max_length=225, null='')),
                ('date', models.DateField(auto_now_add=True)),
                ('join', models.DateTimeField(blank=True)),
            ],
        ),
    ]