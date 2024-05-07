from rest_framework import routers
from application import views

router = routers.SimpleRouter()

router.register('', views.CarsViewSet)
