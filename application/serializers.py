from rest_framework import serializers

from application import models


class Car:
    class List(serializers.ModelSerializer):
        class Meta:
            model = models.Car
            fields = '__all__'

    class Create(serializers.ModelSerializer):
        class Meta:
            model = models.Car
            fields = ['name', 'manufacturer', 'color']

