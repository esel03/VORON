from django.db import models
from account.models import CustomUser
from django.conf import settings
import uuid
import datetime
from advertisement.models import Advertisement



class Provider(models.Model):
    adv = models.OneToOneField(
        Advertisement, default=uuid.uuid4, 
        on_delete = models.CASCADE, primary_key=True)
    title = models.CharField(max_length=240)
    text_in = models.TextField()
    skill_level = models.TextField(blank=True, default=None)
    text_out = models.TextField(blank=True)

    def __str__(self):
        return str(self.adv_id)

    

class Product(models.Model):
    adv = models.OneToOneField(
        Advertisement, default=uuid.uuid4, 
        on_delete = models.CASCADE, primary_key=True)
    title = models.CharField(max_length=240)
    text_in = models.TextField()
    details = models.TextField(blank=True, default=None)
    text_out = models.TextField(blank=True)

    def __str__(self):
        return str(self.adv_id)

    

class Industry(models.Model):
    adv = models.OneToOneField(
        Advertisement, default=uuid.uuid4, 
        on_delete = models.CASCADE, primary_key=True)
    title = models.CharField(max_length=240)
    text_in = models.TextField()
    founding_date = models.CharField(max_length=4, blank=True, default=None)
    text_out = models.TextField(blank=True)

    def __str__(self):
        return str(self.adv_id)

 
# Create your models here.
