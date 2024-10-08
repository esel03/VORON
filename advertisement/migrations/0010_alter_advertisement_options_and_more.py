# Generated by Django 5.1.1 on 2024-10-01 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0009_alter_advertisement_date_finish_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['status_paid', '-price', '-date_create', 'status_done', '-date_start']},
        ),
        migrations.RenameField(
            model_name='advertisement',
            old_name='done',
            new_name='status_done',
        ),
        migrations.RenameField(
            model_name='advertisement',
            old_name='paid',
            new_name='status_paid',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='date_finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 16, 23, 8, 836541)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 2, 16, 23, 8, 836341)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='type_services',
            field=models.CharField(choices=[('услуга', 'provider'), ('товар', 'product'), ('предприятие', 'industry')], max_length=60),
        ),
    ]
