# Generated by Django 5.1.1 on 2024-09-29 04:32

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id_adv', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type_services', models.CharField(max_length=60)),
                ('platforms', models.TextField()),
                ('paid', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('date_create', models.DateTimeField(auto_now=True)),
                ('date_finish', models.DateTimeField(default=datetime.datetime(2024, 10, 6, 4, 32, 28, 809521))),
                ('economic_works', models.TextField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id_industry', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=240)),
                ('text', models.TextField()),
                ('key_adv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.advertisement')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=240)),
                ('text', models.TextField()),
                ('key_adv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.advertisement')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id_provider', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=240)),
                ('text', models.TextField()),
                ('key_adv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.advertisement')),
            ],
        ),
    ]
