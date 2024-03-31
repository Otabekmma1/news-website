from django.urls import path
from .views import addcar, updateCar, deleteCar, brand_car, car

urlpatterns = [

    path('brand/<int:brand_id>/', brand_car, name='bolim'),
    path('add/', addcar, name='addcar'),
    path('update/<id>/', updateCar, name="updatecar"),
    path('delete/<id>/', deleteCar, name="deletecar"),
    path('', car, name='cars'),
]