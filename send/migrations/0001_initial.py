# Generated by Django 4.0.4 on 2022-04-26 08:50

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('phone_operator', models.CharField(max_length=5)),
                ('teg', models.CharField(max_length=150)),
                ('time_zone', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_start', models.DateTimeField()),
                ('text', models.CharField(max_length=150)),
                ('date_time_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_start_message', models.DateTimeField()),
                ('status_message', models.BooleanField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send.client')),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send.distribution')),
            ],
        ),
    ]
