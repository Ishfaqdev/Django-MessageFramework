from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=55)
    password = models.CharField(max_length=33)
    email = models.EmailField(max_length=50)
