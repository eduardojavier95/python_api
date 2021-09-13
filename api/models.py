from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    foto = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    foto = models.CharField(max_length=500)
    precio = models.FloatField()
    rating = models.FloatField()
    descripcion = models.TextField()
    existencia = models.FloatField()
    fecha_venc = models.DateField()
    categoria = models.ForeignKey(to='Categoria', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}"


class Oferta(models.Model):
    nombre = models.CharField(max_length=250)
    foto = models.CharField(max_length=500)
    descripcion = models.TextField()
    descuento = models.FloatField()

    def __str__(self):
        return f"{self.nombre}"


class PreOrden(models.Model):
    orden = models.JSONField()
    fecha = models.DateField()
    periodo = models.IntegerField()

    def __str__(self):
        return f"{self.id}"


class Usuario(models.Model):
    email = models.EmailField()
    user = models.CharField(max_length=250)
    pwd = models.CharField(max_length=250)
    preorden = models.ManyToManyField(to=PreOrden)

    def __str__(self):
        return f"{self.email}"


class Venta(models.Model):
    usuario = models.ForeignKey(to=Usuario, on_delete=models.SET_NULL, null=True)
    preorden = models.ForeignKey(to=PreOrden, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.id}"
