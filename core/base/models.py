from django.db import models
from django.contrib.auth.models import User
import json

    

city_choices = []


with open('base/cities.json', 'r') as f:
    cities_data = json.load(f)
    city_choices = [(city['ville'], city['ville']) for city in cities_data]



class SettingUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='setting_user')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    CIN = models.CharField(unique=True, max_length=8)
    email = models.EmailField(unique=True, null=False, default='')
    city = models.CharField(max_length=100, choices=city_choices)
    bio = models.TextField(null=True)
    current_address = models.CharField(max_length=300)
    avatar = models.ImageField(default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CIN']

    def __str__(self):
        return self.CIN
