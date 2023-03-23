from django.urls import path
from . import views

app_name = 'ejercicio'

urlpatterns = [
    path('', views.header, name='header'),
]

