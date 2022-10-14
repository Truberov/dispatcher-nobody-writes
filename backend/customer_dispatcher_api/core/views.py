from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Transport,
)
from core.serializers import (
    TransportSerializer,
)
from core.pagination import StandardPagination


class TransportListView(generics.ListAPIView):
    """
    GET: Получение списка транспортных средств
    """
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardPagination
    filterset_fields = ('is_active', 'type', )
    search_fields = ('name', 'plate_number', 'characteristic', )
