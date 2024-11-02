from rest_framework.viewsets import ModelViewSet
from apps.usuario.models import Rol, Usuario
from apps.usuario.serializer import RolSerializer, UsuarioSerializer

class RolViewSet(ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer