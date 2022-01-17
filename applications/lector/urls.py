from unicodedata import name
from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('prestamo/', views.RegistrarPrestamo.as_view(), name='prestamos'),
    path('prestamo/multiple', views.AddMultiplePrestamo.as_view(),
         name='prestamos_add_multiple'),

]
