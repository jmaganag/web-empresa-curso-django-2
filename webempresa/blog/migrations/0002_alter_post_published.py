# Generated by Django 4.2.3 on 2023-09-13 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 13, 17, 19, 43, 267101, tzinfo=datetime.timezone.utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
