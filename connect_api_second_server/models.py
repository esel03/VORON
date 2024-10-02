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
    text_out = models.TextField()

    def __str__(self):
        return str(self.id_adv)

    

class Product(models.Model):
    adv = models.OneToOneField(
        Advertisement, default=uuid.uuid4, 
        on_delete = models.CASCADE, primary_key=True)
    title = models.CharField(max_length=240)
    text_in = models.TextField()
    text_out = models.TextField()

    def __str__(self):
        return str(self.id_adv)

    

class Industry(models.Model):
    adv = models.OneToOneField(
        Advertisement, default=uuid.uuid4, 
        on_delete = models.CASCADE, primary_key=True)
    title = models.CharField(max_length=240)
    text_in = models.TextField()
    text_out = models.TextField()

    def __str__(self):
        return str(self.id_adv)

 
# Create your models here.
