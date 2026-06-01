from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permission import IsOwnerOrReadOnly
from .filters import AdvertisementFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action == 'create':
            return [IsAuthenticated()]

        if self.action in ["update", "partial_update", 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [] # оставляет просмотр открытым для всех
