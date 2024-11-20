from rest_framework.routers import DefaultRouter
from apps.trazabilidad.api.views import ActividadViewSet, RealizaViewSet, EspecieViewSet, TipoCultivoViewSet, SemilleroViewSet, AsignacionActividadViewSet, ProgramacionViewSet, NotificacionViewSet, ControlUsoInsumoViewSet, CalendarioLunarViewSet

# Crear routers específicos para cada grupo de ViewSets
router_actividad = DefaultRouter()
router_actividad.register(prefix='actividades', viewset=ActividadViewSet, basename='actividades')

router_realiza = DefaultRouter()
router_realiza.register(prefix='realiza', viewset=RealizaViewSet, basename='realiza')

router_especie = DefaultRouter()
router_especie.register(prefix='especies', viewset=EspecieViewSet, basename='especies')

router_tipo_cultivo = DefaultRouter()
router_tipo_cultivo.register(prefix='tipos_cultivo', viewset=TipoCultivoViewSet, basename='tipos_cultivo')

router_semillero = DefaultRouter()
router_semillero.register(prefix='semilleros', viewset=SemilleroViewSet, basename='semilleros')

router_asignacion_actividad = DefaultRouter()
router_asignacion_actividad.register(prefix='asignaciones_actividades', viewset=AsignacionActividadViewSet, basename='asignaciones_actividades')

router_programacion = DefaultRouter()
router_programacion.register(prefix='programaciones', viewset=ProgramacionViewSet, basename='programaciones')

router_notificacion = DefaultRouter()
router_notificacion.register(prefix='notificaciones', viewset=NotificacionViewSet, basename='notificaciones')

router_control_uso_insumo = DefaultRouter()
router_control_uso_insumo.register(prefix='control_uso_insumos', viewset=ControlUsoInsumoViewSet, basename='control_uso_insumos')

router_calendario_lunar = DefaultRouter()
router_calendario_lunar.register(prefix='calendario_lunar', viewset=CalendarioLunarViewSet, basename='calendario_lunar')

# Exportar los routers como un diccionario
routers = {
    'actividades': router_actividad,
    'realiza': router_realiza,
    'especies': router_especie,
    'tipos_cultivo': router_tipo_cultivo,
    'semilleros': router_semillero,
    'asignaciones_actividades': router_asignacion_actividad,
    'programaciones': router_programacion,
    'notificaciones': router_notificacion,
    'control_uso_insumos': router_control_uso_insumo,
    'calendario_lunar': router_calendario_lunar,
}
