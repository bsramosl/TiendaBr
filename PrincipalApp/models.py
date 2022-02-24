from django.db import models
 
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50,blank=False,null=False)
    descripcion = models.CharField(max_length=50, blank=False, null=False)
    precio = models.CharField(max_length=50, blank=False, null=False)
    foto = models.ImageField('Imagen',upload_to='img/',blank=True, null=True)
    foto1 = models.ImageField('Imagen1',upload_to='img/',blank=True, null=True)
    foto2 = models.ImageField('Imagen2',upload_to='img/',blank=True, null=True)
    foto3 = models.ImageField('Imagen3',upload_to='img/',blank=True, null=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering =['nombre']
    
    def __str__(self):
        return self.nombre



class Categoria (models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
