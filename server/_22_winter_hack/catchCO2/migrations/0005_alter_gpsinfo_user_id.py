# Generated by Django 3.2.5 on 2022-02-03 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catchCO2', '0004_auto_20220204_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpsinfo',
            name='user_id',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gpsinfo', to=settings.AUTH_USER_MODEL),
        ),
    ]