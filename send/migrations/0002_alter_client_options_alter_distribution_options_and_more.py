# Generated by Django 4.0.4 on 2022-04-29 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='distribution',
            options={'verbose_name': 'Distribution', 'verbose_name_plural': 'Distributions'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AddField(
            model_name='distribution',
            name='mobile_codes',
            field=models.CharField(blank=True, max_length=50, verbose_name='Operator code'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='tags',
            field=models.CharField(blank=True, max_length=50, verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(regex='^7\\w{10}$')], verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_operator',
            field=models.PositiveIntegerField(verbose_name='phone_operator'),
        ),
        migrations.AlterField(
            model_name='client',
            name='teg',
            field=models.CharField(blank=True, max_length=50, verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='client',
            name='time_zone',
            field=models.TimeField(max_length=10, verbose_name='time_zone'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='date_time_end',
            field=models.DateTimeField(verbose_name='Start mailing'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='date_time_start',
            field=models.DateTimeField(verbose_name='Start mailing'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_time_start_message',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='status_message',
            field=models.CharField(choices=[('sent', 'Sent'), ('proceeded', 'Proceeded'), ('failed', 'Failed')], max_length=50),
        ),
    ]
