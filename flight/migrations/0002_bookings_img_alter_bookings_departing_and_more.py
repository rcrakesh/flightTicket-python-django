# Generated by Django 5.0.1 on 2024-02-04 13:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookings',
            name='Departing',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='Returning',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]