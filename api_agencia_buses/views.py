from api_agencia_buses.models import Pasajero, Horario, Bus, Chofer, Trayecto, Boleto
from rest_framework import viewsets, generics
from api_agencia_buses.serializers import PasajeroSerializer, ChoferSerializer, TrayectoSerializer, BusSerializer, BoletoSerializer, HorarioSerializer, PasajeroHorarioSerializer, PasajeroBoletoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, F, FloatField
from django.db.models.functions import Cast


class PasajeroViewSet(viewsets.ModelViewSet):

    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer


class HorarioViewSet(viewsets.ModelViewSet):

    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class PasajeroHorarioViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroHorarioSerializer


class PasajeroBoletoViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroBoletoSerializer


class BusViewSet(viewsets.ModelViewSet):

    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusListSet(generics.ListAPIView):
    serializer_class = BusSerializer

    def get_queryset(self):
        queryset = Bus.objects.all()
        boletos_vendidos = self.request.query_params.get(
            'boletos_vendidos', '')

        if boletos_vendidos:
            queryset = Bus.objects.annotate(porcentaje=Cast(
                (Count('Boletos') * 100), FloatField())/Cast(F('Capacidad'), FloatField()))
            return queryset.filter(porcentaje__gte=boletos_vendidos)
        else:
            return queryset


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
