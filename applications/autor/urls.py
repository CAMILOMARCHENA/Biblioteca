from unicodedata import name
from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('autores/', views.ListAutores.as_view(), name='Autores'),

]
