from django.urls import path
from . import views

urlpatterns = [
    path('PasswordGenHome',views.passwordGenHome,name='PasswordGenHome')
]