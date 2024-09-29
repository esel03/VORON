from django.db import models
from account.models import CustomUser
from django.conf import settings
import uuid
import datetime

class Advertisement(models.Model):
    id_adv = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ForeignKey(CustomUser, default=uuid.uuid4, on_delete = models.CASCADE)
    CHOICES_SERVICES = (
        ('услуга', 'provider'),
        ('товар', 'product'),
        ('предприятие', 'indusrty'),
        )
    type_services = models.CharField(max_length=60, choices = CHOICES_SERVICES) #provider, product, industry
    platforms = models.TextField(default='yandex') #яндекс, авито и пр; платформа для размещения рекламы
    paid = models.BooleanField(default=False) # статус оплаты
    price = models.FloatField() #цена компании
    date_create = models.DateTimeField(auto_now=True) #дата создания компании
    date_start = models.DateTimeField(default=datetime.datetime.utcnow() + datetime.timedelta(days=1)) #дата запуска комании 
    date_finish = models.DateTimeField(default=datetime.datetime.utcnow() + datetime.timedelta(days=2)) #дата окончания компании
    economic_works = models.TextField() #сфера эконом деятельности
    done = models.BooleanField(default=False) #завершенность

    class Meta:
        ordering = ["paid", "-price", "-date_create","done", "-date_start"]


    def __str__(self):
        return str(self.id_adv)

    def __str__(self):
        return CustomUser.objects.get(pk=self.users.id_user).email


















