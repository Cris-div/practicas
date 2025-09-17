from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre_empresa=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_empresa
class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
