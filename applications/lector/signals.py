

def update_libro_stock(sender, instance, **kwards):
    '''Actualizamos el stock luego de eliminar un prestamo'''
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()
