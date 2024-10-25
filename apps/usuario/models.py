from django.db import models
from  django.contrib.auth.models import AbstractUser
# Create your models here.
 
class Rol(models.Model):
    opciones=[
        ('Aprendiz','Aprendiz'),
        ('Pasante','Pasante'),
        ('Intructor','Instructor'),
        ('Administrador','Administrador')
        ]
    rol=models.CharField(max_length=20, choices=opciones)
    actualizacion = models.CharField(max_length=50)
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.rol
    
class Usuario(AbstractUser):
    
    rol=models.ForeignKey(Rol, on_delete=models.SET_NULL,null=True)


