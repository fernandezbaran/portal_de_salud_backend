from django.db import models

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Pacientes(models.Model):
	nombre=models.CharField(max_length=30)
	direccion=models.CharField(max_length=50,verbose_name="La dirección")
	email=models.EmailField(blank=True,null=True)
	telefono=models.CharField(max_length=7)

def __str__(self):
	return self.nombre

class Imagenes(models.Model):
	estudio=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=100)
	diagnostico=models.CharField(max_length=100)

class Medicacion(models.Model):
	droga=models.CharField(max_length=100)
	prospecto=models.CharField(max_length=100)
	dosis=models.CharField(max_length=100)
