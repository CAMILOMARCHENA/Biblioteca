from unicodedata import name
from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='Libros'),
    path('libros-2/', views.ListLibros.as_view(), name='Libros2'),
    path('libro-detalle/<pk>/', views.LibroDetailView.as_view(), name='libro-detalle'),
    path('libros-trg/', views.ListLibrosTrg.as_view(), name='libros-trg'),

]
