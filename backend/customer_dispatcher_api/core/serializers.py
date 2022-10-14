from rest_framework import serializers

from core.models import Transport, Performer


class PerformerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performer
        fields = '__all__'


class TransportSerializer(serializers.ModelSerializer):
    performer = PerformerSerializer

    class Meta:
        model = Transport
        fields = '__all__'
