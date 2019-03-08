# Generated by Django 2.0.13 on 2019-03-03 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Placa', models.CharField(max_length=35)),
                ('Capacidad', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApellidoPaterno', models.CharField(max_length=35)),
                ('ApellidoMaterno', models.CharField(max_length=35)),
                ('PrimerNombre', models.CharField(max_length=35)),
                ('SegundoNombre', models.CharField(max_length=35)),
                ('RUT', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HoraInicio', models.TimeField()),
                ('HoraFin', models.TimeField()),
                ('Bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_agencia_buses.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApellidoPaterno', models.CharField(max_length=35)),
                ('ApellidoMaterno', models.CharField(max_length=35)),
                ('PrimerNombre', models.CharField(max_length=35)),
                ('SegundoNombre', models.CharField(max_length=35)),
                ('RUT', models.CharField(max_length=8)),
                ('Sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Trayecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=35)),
                ('CiudadSalida', models.CharField(max_length=35)),
                ('CiudadDestino', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='horario',
            name='Trayecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_agencia_buses.Trayecto'),
        ),
        migrations.AddField(
            model_name='bus',
            name='Chofer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_agencia_buses.Chofer'),
        ),
        migrations.AddField(
            model_name='boleto',
            name='Bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_agencia_buses.Bus'),
        ),
        migrations.AddField(
            model_name='boleto',
            name='Pasajero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_agencia_buses.Pasajero'),
        ),
    ]
