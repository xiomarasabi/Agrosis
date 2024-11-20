from rest_framework import viewsets
from apps.trazabilidad.models import Actividad, Realiza, Especie, TipoCultivo, Semillero, AsignacionActividades, Programacion, Notificacion, ControlUsoInsumo, CalendarioLunar
from .serializers import ActividadSerializer, RealizaSerializer, EspecieSerializer, TipoCultivoSerializer, SemilleroSerializer, AsignacionActividadSerializer, ProgramacionSerializer, NotificacionSerializer, ControlUsoInsumoSerializer,CalendarioLunarSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class RealizaViewSet(viewsets.ModelViewSet):
    queryset = Realiza.objects.all()
    serializer_class = RealizaSerializer

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class TipoCultivoViewSet(viewsets.ModelViewSet):
    queryset = TipoCultivo.objects.all()
    serializer_class = TipoCultivoSerializer

class SemilleroViewSet(viewsets.ModelViewSet):
    queryset = Semillero.objects.all()
    serializer_class = SemilleroSerializer

class AsignacionActividadViewSet(viewsets.ModelViewSet):
    queryset = AsignacionActividades.objects.all()
    serializer_class = AsignacionActividadSerializer

class ProgramacionViewSet(viewsets.ModelViewSet):
    queryset = Programacion.objects.all()
    serializer_class = ProgramacionSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class ControlUsoInsumoViewSet(viewsets.ModelViewSet):
    queryset = ControlUsoInsumo.objects.all()
    serializer_class = ControlUsoInsumoSerializer

class CalendarioLunarViewSet(viewsets.ModelViewSet):
    queryset = CalendarioLunar.objects.all()
    serializer_class = CalendarioLunarSerializer
