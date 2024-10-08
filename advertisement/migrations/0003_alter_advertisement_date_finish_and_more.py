# Generated by Django 5.1.1 on 2024-09-29 19:30

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_remove_product_key_adv_remove_provider_key_adv_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='date_finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 1, 19, 30, 11, 891608)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 30, 19, 30, 11, 891409)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='users',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
