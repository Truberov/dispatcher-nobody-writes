from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Transport, Reservation,
)
from core.serializers import (
    TransportSerializer, ReservationSerializer, CharacteristicSerializer, ReservationPostSerializer, TypesSerializer,
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
    filterset_fields = (
        'is_active',
        'type',
        'status',
    )
    search_fields = (
        'name',
        'plate_number',
        'characteristic',
    )


class TypesListView(generics.ListAPIView):
    """
    GET: Получение списка типов ТС
    """
    serializer_class = TypesSerializer
    permission_classes = ()

    def get_queryset(self):
        return Transport.objects.all().values('type').distinct()


class CharacteristicListView(generics.ListAPIView):
    """
    GET: Получение списка характеристик и типов ТС
    """
    serializer_class = CharacteristicSerializer
    permission_classes = ()
    filterset_fields = ('type', )

    def get_queryset(self):
        return Transport.objects.all().values(
            'type',
            'characteristic',
        )


class ReservationListCreatView(generics.ListCreateAPIView):
    """
    GET: Получить список заявок на брони
    POST: Создать заявку на бронь
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationPostSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardPagination
    filterset_fields = ()
    search_fields = ()

    def perform_create(self, serializer):
        serializer.save()
