from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=30, default="")
    subtitulo = models.TextField(max_length=90, default="")
    cuerpo = models.TextField(max_length=1000, default="")
    autor = models.CharField(max_length=30, default="")
    fecha = models.DateField()
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo+" "+self.subtitulo+" "+self.autor

class Autor(models.Model):
    nombre = models.CharField(max_length=30, default="")
    apellido = models.CharField(max_length=30 , default="")
    profesion = models.CharField(max_length=30 , default="")
    email = models.EmailField(default="")
    def __str__(self) -> str:
        return self.nombre+" "+self.apellido

class Invitados(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30 , default="")
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre
    
