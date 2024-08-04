from django.urls import path

from . import views

urlpatterns = [
    path('todoHome',views.todoHome,name='todoHome'),
    path('deleteTodo',views.deleteTodo,name='deleteTodo'),
    path('updateForm',views.updateForm,name='updateForm'),
    path('updateTodo',views.updateTodo,name='udateTodo')
]