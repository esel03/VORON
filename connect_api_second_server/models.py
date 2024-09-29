from django.db import models
from account.models import CustomUser
from django.conf import settings
import uuid
import datetime
from advertisement.models import Advertisement



class Provider(models.Model):
    id_provider = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    key_adv = models.ForeignKey(Advertisement, on_delete = models.CASCADE)
    title = models.CharField(max_length=240)
    text_in = models.TextField()
    text_out = models.TextField()

    def __str__(self):
        return self.id_provider


class Product(models.Model):
    id_product = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    key_adv = models.ForeignKey(Advertisement, on_delete = models.CASCADE)
    title = models.CharField(max_length=240)
    text_in = models.TextField()
    text_out = models.TextField()

    def __str__(self):
        return self.id_product


class Industry(models.Model):
    id_industry = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    key_adv = models.ForeignKey(Advertisement, on_delete = models.CASCADE)
    title = models.CharField(max_length=240)
    text_in = models.TextField()
    text_out = models.TextField()

    def __str__(self):
        return self.id_industry
# Create your models here.
