# Generated by Django 5.1.1 on 2024-10-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0012_alter_advertisement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='date_finish',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='date_start',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(default='Проект_2024-10-01 17:54:03.945345', max_length=60),
        ),
    ]
