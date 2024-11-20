from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActividadViewSet, RealizaViewSet, EspecieViewSet, TipoCultivoViewSet, SemilleroViewSet, AsignacionActividadViewSet, ProgramacionViewSet, NotificacionViewSet, ControlUsoInsumoViewSet

router = DefaultRouter()
router.register(r'actividades', ActividadViewSet)
router.register(r'realiza', RealizaViewSet)
router.register(r'especies', EspecieViewSet)
router.register(r'tipos_cultivo', TipoCultivoViewSet)
router.register(r'semilleros', SemilleroViewSet)
router.register(r'asignaciones_actividades', AsignacionActividadViewSet)
router.register(r'programaciones', ProgramacionViewSet)
router.register(r'notificaciones', NotificacionViewSet)
router.register(r'control_uso_insumos', ControlUsoInsumoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
