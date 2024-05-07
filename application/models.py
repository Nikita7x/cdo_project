from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True)