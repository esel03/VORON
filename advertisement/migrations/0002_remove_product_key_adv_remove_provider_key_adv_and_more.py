# Generated by Django 5.1.1 on 2024-09-29 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='key_adv',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='key_adv',
        ),
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['paid', '-price', '-date_create', 'done', '-date_start']},
        ),
        migrations.AddField(
            model_name='advertisement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 30, 18, 28, 50, 747681)),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='date_finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 1, 18, 28, 50, 747944)),
        ),
        migrations.DeleteModel(
            name='Industry',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Provider',
        ),
    ]
