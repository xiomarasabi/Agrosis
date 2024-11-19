from django.db import models

# Create your models here.

class Actividad(models.Model):
    nombre_actividad = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_actividad


class Realiza(models.Model):
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True)
    fk_id_actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, null=True) 
    
    def __str__(self):
        return f'{self.fk_id_cultivo}{self.fk_id_actividad}'
    

class TipoCultivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Especie(models.Model):
    nombre_comun = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=100)
    descripcion = models.TextField()
    fk_id_tipo_cultivo = models.ForeignKey(TipoCultivo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_comun

class Semillero(models.Model):
    nombre_semillero = models.CharField(max_length=100)
    fecha_siembra = models.DateField() 
    fecha_estimada = models.DateField() 
    cantidad = models.IntegerField() 

    def __str__(self): return self.nombre_semillero

class AsignacionActividades(models.Model):
    fecha = models.DateField()
    observaciones = models.TextField() 
    fk_id_actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    id_identificacion = models.ForeignKey(Identificacion, on_delete=models.CASCADE)
    
    def __str__(self): return f'{self.fk_id_actividad} - {self.id_identificacion}'

class CalendarioLunar(models.Model):
    fecha = models.DateField()
    descripcion_evento = models.TextField()
    evento = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.evento} - {self.fecha}'

class Programacion(models.Model): 
    estado = models.CharField(max_length=50) 
    fecha_programada = models.DateTimeField() 
    duracion = models.DurationField()
    fk_id_asignacionActividades = models.ForeignKey(AsignacionActividades, on_delete=models.CASCADE)
    fk_id_calendario = models.ForeignKey(CalendarioLunar, on_delete=models.CASCADE) 
    
    def __str__(self): return f'{self.estado} - {self.fecha_programada}'

class Notificacion(models.Model):
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    fk_id_programacion = models.ForeignKey(Programacion, on_delete=models.CASCADE) 
    
    def __str__(self): return self.titulo

class ControlUsoInsumo(models.Model):
    fk_id_insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE) 
    fk_id_control_fitosanitario = models.ForeignKey(ControlFitosanitario, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self): return f'{self.fk_id_insumo} - {self.cantidad}'