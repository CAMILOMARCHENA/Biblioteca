from django.db import models
from django.db.models import Q, Count, Avg
import datetime


class PrestamoManager(models.Manager):
    '''procedimiento para el prestamo'''

    def promedio_edades(self):
        resultado = self.filter(libro__id='8').aggregate(
            promedio_edad=Avg('lector__edad')
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados=Count('libro')
        ).annonate(num_prestados=Count('libro'))
        for r in resultado:
            print('*******')
            print(r, r['num_prestados'])
            return resultado
