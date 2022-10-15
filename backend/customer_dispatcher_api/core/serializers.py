from rest_framework import serializers

from core.models import (
    Transport, Performer, Reservation,
)


class PerformerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performer
        fields = '__all__'


class TransportSerializer(serializers.ModelSerializer):
    performer = PerformerSerializer

    class Meta:
        model = Transport
        fields = '__all__'


class TypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transport
        fields = ('type', )


class CharacteristicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transport
        fields = ('type', 'characteristic', )


class ReservationFeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transport
        fields = ('type', 'characteristic', )


class ReservationSerializer(serializers.ModelSerializer):
    transport = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = '__all__'


class ReservationPostSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Reservation
        fields = ('characteristic', 'type', 'end_date', 'transport', 'status', )

