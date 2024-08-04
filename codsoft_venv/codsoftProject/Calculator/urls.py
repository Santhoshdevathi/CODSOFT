from django.urls import path

from . import views

urlpatterns = [
    path('CalculatorHome',views.Calculations,name='CalculatorHome'),
    path('',views.home),
    path('home',views.home,name='home')
]