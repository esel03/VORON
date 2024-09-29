from django.test import TestCase
from rest_framework.test import APIClient

client = APIClient()
client.post('/api/add/', {'id_user': '4343', 'entry': 'Тоска'}, format='json')

#{'id_user': '4343', 'entry': 'Тоска'}