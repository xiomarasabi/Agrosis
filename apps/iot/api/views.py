from rest_framework.viewsets import ModelViewSet
from apps.iot.models import Sensores, Mide
from apps.iot.api.serializers import SensoresSerializer,MideSerializer

class SensoresViewSet(ModelViewSet):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer

class MideViewSet(ModelViewSet):
    queryset = Mide.objects.all()
    serializer_class = MideSerializer