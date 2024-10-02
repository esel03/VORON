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
        ('предприятие', 'industry'),
        )
    title = models.CharField(max_length=60, default=f'Проект_{datetime.datetime.utcnow()}')
    type_services = models.CharField(max_length=60, choices = CHOICES_SERVICES) #provider, product, industry
    platforms = models.TextField(default='yandex') #яндекс, авито и пр; платформа для размещения рекламы
    status_paid = models.BooleanField(default=False) # статус оплаты
    price = models.FloatField() #цена компании
    date_create = models.DateTimeField(auto_now=True) #дата создания компании
    date_start = models.DateTimeField(blank=True) #дата запуска комании 
    date_finish = models.DateTimeField(blank=True) #дата окончания компании
    economic_works = models.TextField() #сфера эконом деятельности
    status_done = models.BooleanField(default=False) #завершенность

    class Meta:
        ordering = ["status_paid", "-price", "-date_create", "status_done", "-date_start"]


    def str(self):
        return f"{CustomUser.objects.get(pk=self.users.id_user).email},  {self.platforms},  {self.type_services},  {self.id_adv}, {self.date_create}, {self.date_start}, {self.date_finish}"


















