import io
import csv
import json

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, renderers

from application import models
from application import serializers


class CarsViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    renderer_classes = [renderers.JSONRenderer]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.Car.Create
        return serializers.Car.List

    def list(self, request, *args, **kwargs):
        cars = self.get_queryset()
        serializer = self.get_serializer(cars, many=True)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=output.csv'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(serializer.data[0].keys())

        for item in serializer.data:
            writer.writerow(item.values())

        return response
