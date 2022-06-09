from django.db import models

class Medico(models.Model):
    #charfield campo de texto
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    edad = models.IntegerField()  #campo numerico

    def __str__(self) -> str:
        return self.nombre+" "+self.apellido+" "+self.especialidad

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()  #campo numerico
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" "+self.apellido

class Clinica(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" "+self.direccion
    
