from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=30, default="")
    apellido = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")
    def __str__(self) -> str:
        return self.nombre+" "+self.apellido

class Medico(models.Model):
    nombre = models.CharField(max_length=30, default="")
    apellido = models.CharField(max_length=30 , default="")
    profesion = models.CharField(max_length=30 , default="")
    email = models.EmailField(default="")
    def __str__(self) -> str:
        return self.nombre+" "+str(self.profesion)

class Clinica(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" "+self.direccion
    
