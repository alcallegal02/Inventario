# Generated by Django 5.1.3 on 2024-12-19 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='fecha_entrega',
            field=models.DateField(default=datetime.date.today),
        ),
    ]