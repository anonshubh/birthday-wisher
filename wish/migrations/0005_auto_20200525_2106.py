# Generated by Django 2.2.12 on 2020-05-25 15:36

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0004_birthday_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]
