from api_agencia_buses.models import Pasajero, Horario, Bus, Chofer, Trayecto, Boleto
from rest_framework import viewsets
from api_agencia_buses.serializers import PasajeroSerializer, ChoferSerializer, TrayectoSerializer, BusSerializer, BoletoSerializer, HorarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PasajeroViewSet(viewsets.ModelViewSet):

    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer


class HorarioViewSet(viewsets.ModelViewSet):

    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class BusViewSet(viewsets.ModelViewSet):

    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class ChoferViewSet(viewsets.ModelViewSet):

    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer


class TrayectoViewSet(viewsets.ModelViewSet):

    queryset = Trayecto.objects.all()
    serializer_class = TrayectoSerializer

    # @action(detail=True, methods=['get'])
    # def promedio(self, request, pk=None):
    #     horarios_pk = Horario.objects.all().filter(Trayecto=pk)
    #     total_boletos = 0
    #     total_bus = horarios_pk.count()
    #     for horario in horarios_pk:
    #         total_boletos += horario.Bus.boletos.all().count()
    #     return Response({'promedio': total_boletos/total_bus})


class BoletoViewSet(viewsets.ModelViewSet):

    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer
