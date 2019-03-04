from api_agencia_buses.models import Pasajero, Horario, Bus, Chofer, Trayecto, Boleto
from rest_framework import serializers


class PasajeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pasajero
        fields = ('url', 'ApellidoPaterno', 'ApellidoMaterno',
                  'PrimerNombre', 'SegundoNombre', 'RUT', 'Sexo')


class ChoferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chofer
        fields = ('url', 'ApellidoPaterno', 'ApellidoMaterno',
                  'PrimerNombre', 'SegundoNombre', 'RUT')


class BoletoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boleto
        fields = ('url', 'Fecha', 'Pasajero', 'Bus')


class BusSerializer(serializers.HyperlinkedModelSerializer):
    Vendidos = serializers.SerializerMethodField()

    class Meta:
        model = Bus
        fields = ('url', 'Placa', 'Chofer', 'Capacidad', 'boletos', 'Vendidos')

    boletos = BoletoSerializer(many=True, read_only=True)

    def get_Vendidos(self, obj):
        total_boletos = obj.boletos.all().count()

        porcentaje_vendidos = (total_boletos * 100)/obj.Capacidad

        return porcentaje_vendidos


class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ('url', 'HoraInicio', 'HoraFin', 'Trayecto', 'Bus')

    Bus = BusSerializer(many=False, read_only=True)


class TrayectoSerializer(serializers.HyperlinkedModelSerializer):
    Promedio = serializers.SerializerMethodField()

    class Meta:
        model = Trayecto
        fields = ('url', 'Nombre', 'CiudadSalida',
                  'CiudadDestino', 'horarios', 'Promedio')

    # buses = serializers.PrimaryKeyRelatedField(many=True, queryset=buses.objects.all())
    horarios = HorarioSerializer(many=True, read_only=True)

    def get_Promedio(self, obj):
        total_boletos = 0
        total_bus = obj.horarios.all().count()

        for horario in obj.horarios.all():
            total_boletos += horario.Bus.boletos.all().count()
        return total_boletos/total_bus
