# Generated by Django 5.0.1 on 2024-02-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('From', models.CharField(max_length=200)),
                ('To', models.CharField(max_length=200)),
                ('Departing', models.DateField()),
                ('Returning', models.DateField()),
                ('Adults', models.SmallIntegerField()),
                ('Children', models.SmallIntegerField()),
                ('travelclass', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
    ]
