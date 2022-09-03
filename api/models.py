import email

from django.db import models


# Create your models here.


class Login(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Company(models.Model):
    nombre = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.nombre


