# Generated by Django 4.2.6 on 2024-08-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_beting_withdrawal_games_result_games_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarlineGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null='')),
                ('chart', models.CharField(blank=True, max_length=225, null='')),
                ('result', models.CharField(blank=True, max_length=225, null='')),
                ('status', models.CharField(blank=True, max_length=225, null='')),
            ],
        ),
        migrations.AddField(
            model_name='games',
            name='chart',
            field=models.CharField(blank=True, max_length=225, null=''),
        ),
    ]