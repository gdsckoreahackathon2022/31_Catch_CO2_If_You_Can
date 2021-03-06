# Generated by Django 4.0.1 on 2022-02-04 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emissions_list',
            fields=[
                ('act', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('unit', models.PositiveIntegerField()),
                ('emissions', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_emissions',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('act', models.CharField(max_length=100)),
                ('freq', models.PositiveIntegerField()),
                ('sum', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
