from django.db import models
from applications.autor.models import Autor
from django.db.models.signals import post_save
from .managers import LibroManager, CategoriaManager
from PIL import Image

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=30, blank=True)
    objects = CategoriaManager()

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, blank=True, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField('Título', max_length=50)
    fecha = models.DateField('Fecha de lanzamiento',
                             auto_now=False, auto_now_add=False)
    portada = models.ImageField(
        'Portada', upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)
    objects = LibroManager()
    visitas = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id) + ' - ' + self.titulo


def optimize_image(sender, instance, **kwards):

    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)


post_save.connect(optimize_image, sender=Libro)
