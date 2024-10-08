# Generated by Django 5.1.1 on 2024-09-29 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_alter_advertisement_date_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='date_finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 1, 22, 8, 1, 311114)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 30, 22, 8, 1, 310493)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='platforms',
            field=models.TextField(default='yandex'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='type_services',
            field=models.CharField(choices=[('услуга', 'provider'), ('товар', 'product'), ('предприятие', 'indusrty')], max_length=60),
        ),
    ]
