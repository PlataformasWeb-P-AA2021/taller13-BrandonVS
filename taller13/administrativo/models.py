from django.db import models


# Create your models here.
class Edificio(models.Model):
    opciones_edifico = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial')
    )

    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=opciones_edifico)

    def __str__(self):
        return "%s - %s - %s - %s" % (self.nombre,
                                      self.direccion,
                                      self.ciudad,
                                      self.tipo)


class Departamento(models.Model):
    nombre_prop = models.CharField(max_length=50)
    costo = models.IntegerField()
    cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
                                 related_name="departamentos")

    def __str__(self):
        return "%s - %s - %s" % (self.nombre_prop,
                                 self.costo,
                                 self.cuartos)