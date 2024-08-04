from django.urls import path

from . import views

urlpatterns = [
    path('GameHome',views.GameHome,name='GameHome'),
    path('quitGame',views.quitGame,name='quitGame'),
    path('newGame',views.newGame)
]