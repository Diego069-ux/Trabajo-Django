from django.db import models

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=100)
nacionalidad = models.CharField(max_length=100)

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True)
bio = models.TextField(blank=True, null=True)

class Comuna(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
nombre = models.CharField(max_length=100)




class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
calle = models.CharField(max_length=200)
numero = models.CharField(max_length=10)
departamento = models.CharField(max_length=10, blank=True, null=True)

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=150)
direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
paginas = models.PositiveIntegerField()
copias = models.PositiveIntegerField()
biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
habilitado = models.BooleanField(default=True)

class Lector(models.Model):
    rut = models.CharField(max_length=12, unique=True) # Ejemplo: 12345678-9
nombre = models.CharField(max_length=150)
direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)
biblioteca = models.ForeignKey(Biblioteca, on_delete=models.SET_NULL, null=True)
habilitado = models.BooleanField(default=True)

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
fecha_prestamo = models.DateTimeField(auto_now_add=True)
plazo_devolucion = models.DateTimeField()
fecha_entrega = models.DateTimeField(blank=True, null=True)