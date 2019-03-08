from api_agencia_buses.models import Pasajero, Horario, Bus, Chofer, Trayecto, Boleto
from rest_framework import serializers


class PasajeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pasajero
        fields = ('url', 'ApellidoPaterno', 'ApellidoMaterno',
                  'PrimerNombre', 'SegundoNombre', 'RUT', 'Sexo')


class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ('url', 'HoraInicio', 'HoraFin', 'Trayecto', 'Bus')


class BoletoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boleto
        fields = ('url', 'Fecha', 'Bus', 'Pasajero')


class PasajeroBoletoSerializer(serializers.ModelSerializer):
    boletos = BoletoSerializer(many=False, write_only=True)

    class Meta:
        model = Pasajero
        fields = ('url', 'ApellidoPaterno', 'ApellidoMaterno',
                  'PrimerNombre', 'SegundoNombre', 'RUT', 'Sexo', 'boletos')


class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ('url', 'HoraInicio', 'HoraFin', 'Trayecto', 'Bus')


class BoletoASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boleto
        fields = ('url', 'Fecha', 'Bus')


class PasajeroBoletoSerializer(serializers.ModelSerializer):
    boletos = BoletoASerializer(many=False, write_only=True)

    class Meta:
        model = Pasajero
        fields = ('url', 'ApellidoPaterno', 'ApellidoMaterno',
                  'PrimerNombre', 'SegundoNombre', 'RUT', 'Sexo', 'boletos')

    def create(self, validated_data):
        boletos_data = validated_data.pop('boletos')
        pasajero = Pasajero.objects.create(**validated_data)
        Boleto.objects.create(Pasajero=pasajero, **boletos_data)
        return pasajero

    # def update(self, instance, validated_data):
    #     boletos_data = validated_data.pop('boletos')
    #     #print(boletos_data)
    #     #print(instance)
    #     boleto = instance.boletos
    #     instance.PrimerNombre = validated_data.get(
    #         'PrimerNombre', instance.PrimerNombre)
    #     instance.save()
    #     #print(boletos_data)
    #     #boleto.Fecha = boletos_data.get('Fecha', boleto.Fecha)
    #     #boleto.save()
    #     return instance


class PasajeroHorarioSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer(many=False, write_only=True)

    class Meta:
        model = Pasajero
        fields = ('url', 'ApellidoPaterno', 'ApellidoMaterno',
                  'PrimerNombre', 'SegundoNombre', 'RUT', 'Sexo', 'horarios')

    def create(self, validated_data):
        horarios_data = validated_data.pop('horarios')
        pasajero = Pasajero.objects.create(**validated_data)
        print(horarios_data)
        for horario_data in horarios_data:
            Pasajero.objects.create(pasajero=pasajero, *horario_data)
        return pasajero


class PasajeroHorarioSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer(many=False, write_only=True)

    class Meta:
        model = Pasajero
        fields = ('url', 'ApellidoPaterno', 'ApellidoMaterno',
                  'PrimerNombre', 'SegundoNombre', 'RUT', 'Sexo', 'horarios')

    def create(self, validated_data):
        horarios_data = validated_data.pop('horarios')
        pasajero = Pasajero.objects.create(**validated_data)
        print(horarios_data)
        for horario_data in horarios_data:
            Pasajero.objects.create(pasajero=pasajero, *horario_data)
        return pasajero


class ChoferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chofer
        fields = ('url', 'ApellidoPaterno', 'ApellidoMaterno',
                  'PrimerNombre', 'SegundoNombre', 'RUT')


class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = ('url', 'Placa', 'Chofer', 'Capacidad',
                  'Boletos', 'PorcentajeVendido')

    Boletos = BoletoSerializer(many=True, read_only=True)
    PorcentajeVendido = serializers.SerializerMethodField()

    def get_PorcentajeVendido(self, obj):
        total_boletos = obj.Boletos.all().count()

        porcentaje_vendidos = (total_boletos * 100)/obj.Capacidad

        return porcentaje_vendidos


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
            total_boletos += horario.Bus.Boletos.all().count()
        if total_bus > 0:
            promedio = total_boletos/total_bus
        else:
            promedio = 0
        return promedio
