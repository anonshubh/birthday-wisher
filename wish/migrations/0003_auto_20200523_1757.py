# Generated by Django 2.2.12 on 2020-05-23 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0002_auto_20200523_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='wisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
