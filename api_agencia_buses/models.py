from django.db import models


class Pasajero(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    PrimerNombre = models.CharField(max_length=35)
    SegundoNombre = models.CharField(max_length=35)
    RUT = models.CharField(max_length=8)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='F')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

        def __str__(self):
            return self.NombreCompleto()


class Chofer(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    PrimerNombre = models.CharField(max_length=35)
    SegundoNombre = models.CharField(max_length=35)
    RUT = models.CharField(max_length=8)


class Trayecto(models.Model):
    Nombre = models.CharField(max_length=35)
    CiudadSalida = models.CharField(max_length=35)
    CiudadDestino = models.CharField(max_length=35)

    def __str__(self):
        return "{0}".format(self.Nombre)


class Bus(models.Model):
    Placa = models.CharField(max_length=35)
    Chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    Capacidad = models.PositiveSmallIntegerField()


class Boleto(models.Model):
    Fecha = models.DateField()
    Pasajero = models.ForeignKey(
        Pasajero, null=False, blank=False, on_delete=models.CASCADE)
    Bus = models.ForeignKey(Bus, null=False, blank=False,
                            on_delete=models.CASCADE, related_name='Boletos')


class Horario(models.Model):
    HoraInicio = models.TimeField(auto_now=False)
    HoraFin = models.TimeField(auto_now=False)
    Trayecto = models.ForeignKey(
        Trayecto, null=False, blank=False, on_delete=models.CASCADE, related_name='horarios')
    Bus = models.ForeignKey(
        Bus, null=False, blank=False, on_delete=models.CASCADE, related_name='horarios')
