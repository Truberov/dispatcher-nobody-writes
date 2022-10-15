from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Transport, Reservation,
)
from core.serializers import (
    TransportSerializer, ReservationSerializer,
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
    filterset_fields = ('is_active', 'type', 'status', )
    search_fields = ('name', 'plate_number', 'characteristic', )


class ReservationListCreatView(generics.ListCreateAPIView):
    """
    GET: Получить список заявок на брони
    POST: Создать заявку на бронь
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardPagination
    filterset_fields = ()
    search_fields = ()

    def perform_create(self, serializer):
        serializer.save()
