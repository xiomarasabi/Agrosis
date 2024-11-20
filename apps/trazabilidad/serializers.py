from rest_framework import serializers
from .models import Actividad, Realiza, Especie, TipoCultivo, Semillero, AsignacionActividades, Programacion, Notificacion, ControlUsoInsumo

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

class RealizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realiza
        fields = '__all__'

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'

class TipoCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCultivo
        fields = '__all__'

class SemilleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semillero
        fields = '__all__'

class AsignacionActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionActividades
        fields = '__all__'

class ProgramacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programacion
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class ControlUsoInsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlUsoInsumo
        fields = '__all__'
