from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page),
    path('calculator', include('calc.urls'))
]