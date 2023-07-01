from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} / Camada: {self.camada}"
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} / Apellido: {self.apellido}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    materia = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} / Materia: {self.materia}"

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.avatar}"