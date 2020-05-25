# Generated by Django 2.2.12 on 2020-05-25 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0005_auto_20200525_2106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='birthday',
            options={'ordering': ['name', '-timestamp']},
        ),
        migrations.AddField(
            model_name='birthday',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]