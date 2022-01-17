from django.db import models
from django.db.models import Q


class AutorManager(models.Manager):
    '''Managers para el modelo de Autor'''

    def buscar_autor(self, kword):
        resultado = self.filter(nombre__icontains=kword)
        return resultado

    def buscar_autor2(self, kword):
        '''filtro con operador 2'''
        resultado = self.filter(Q(nombre__icontains=kword)
                                | Q(apellidos__icontains=kword))
        return resultado

    def buscar_autor3(self, kword):
        resultado = self.filter(nombre__icontains=kword).exclude(edad=100)
        return resultado

    def buscar_autor4(self, kword):
        '''(gt) mayor que coma es y , (lt) menor que'''
        resultado = self.filter(edad__gt=60, edad__lt=65).order_by(
            'nombre', 'apellidos')
        return resultado
