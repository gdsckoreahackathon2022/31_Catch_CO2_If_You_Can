# Generated by Django 3.2.5 on 2022-02-05 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_emissions',
            name='act',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.emissions_list'),
        ),
    ]
