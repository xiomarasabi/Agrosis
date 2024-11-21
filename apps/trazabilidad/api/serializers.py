from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.models import Actividad, Realiza, Especie, TipoCultivo, Semillero, AsignacionActividades, Programacion, Notificacion, ControlUsoInsumo,CalendarioLunar,Ubicacion,Lote,Eras,Plantacion,Desarrollan,Pea,Desarrollan,Tipo_residuos,Cultivo,Residuos,Control_fitosanitario

class ActividadSerializer(ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

class RealizaSerializer(ModelSerializer):
    class Meta:
        model = Realiza
        fields = '__all__'

class EspecieSerializer(ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'

class TipoCultivoSerializer(ModelSerializer):
    class Meta:
        model = TipoCultivo
        fields = '__all__'

class SemilleroSerializer(ModelSerializer):
    class Meta:
        model = Semillero
        fields = '__all__'

class AsignacionActividadSerializer(ModelSerializer):
    class Meta:
        model = AsignacionActividades
        fields = '__all__'

class ProgramacionSerializer(ModelSerializer):
    class Meta:
        model = Programacion
        fields = '__all__'

class NotificacionSerializer(ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class ControlUsoInsumoSerializer(ModelSerializer):
    class Meta:
        model = ControlUsoInsumo
        fields = '__all__'

class CalendarioLunarSerializer(ModelSerializer):
    class Meta:
        model = CalendarioLunar
        fields = '__all__'
        
        
class UbicacionSerializer(ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'
        
class LoteSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'
        
class ErasSerializer(ModelSerializer):
    class Meta:
        model = Eras
        fields = '__all__'
        
class CultivoSerializer(ModelSerializer):
    class Meta:
        model = Cultivo
        fields = '__all__'
class PlantacionSerializer(ModelSerializer):
    class Meta:
        model = Plantacion
        fields = '__all__'
        
class PeaSerializer(ModelSerializer):
    class Meta:
        model = Pea
        fields = '__all__'
        
class DesarrollanSerializer(ModelSerializer):
    class Meta:
        model = Desarrollan
        fields = '__all__'
        
class Tipo_residuosSerializer(ModelSerializer):
    class Meta:
        model = Tipo_residuos
        fields = '__all__'
        
class ResiduosSerializer(ModelSerializer):
    class Meta:
        model = Residuos
        fields = '__all__'
        
class Control_fitosanitarioSerializer(ModelSerializer):
    class Meta:
        model = Control_fitosanitario
        fields = '__all__'
        
