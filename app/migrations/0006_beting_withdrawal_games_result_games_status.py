# Generated by Django 4.2.6 on 2024-08-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null='')),
                ('pana_name', models.CharField(blank=True, max_length=225, null='')),
                ('digit', models.CharField(blank=True, max_length=225, null='')),
                ('points', models.CharField(blank=True, max_length=225, null='')),
                ('gametype', models.CharField(blank=True, max_length=225, null='')),
                ('status', models.CharField(blank=True, max_length=225, null='')),
                ('join', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=225, null='')),
                ('amount', models.CharField(blank=True, max_length=225, null='')),
                ('status', models.CharField(blank=True, max_length=225, null='')),
                ('join', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='games',
            name='result',
            field=models.CharField(blank=True, max_length=225, null=''),
        ),
        migrations.AddField(
            model_name='games',
            name='status',
            field=models.CharField(blank=True, max_length=225, null=''),
        ),
    ]