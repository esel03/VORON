# Generated by Django 5.1.1 on 2024-10-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0013_alter_advertisement_date_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(default='Проект_2024-10-02 10:18:26.846334', max_length=60),
        ),
    ]
