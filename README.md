# API PASAJES

## Dependencias

Recomendamos la instalación de _Python_ en su última versión 3.7.2. Encontrará un instalador para su sistema operativo en la siguiente dirección: https://www.python.org/downloads/release/python-372/.

## Instalación

1.  `pip install virtualenv` para la instalacion de la herramienta _virtualenv_.
2.  `virtualenv api-pasajes` para la creación de un ambiente aislado para la instalación de dependencias.
3.  Si esta usando un ambiente linux hacer `source api-pasajes/bin/activate` para activar el ambiente. En caso de usar windows puede hacer `source api-pasajes/Scripts/activate`.
4.  `pip install django` para instalar _Django_.
5.  `pip install djangorestframework`.
6.  `pip install django-cors-headers` para manejo de peticiones.(sqlite).
7.  `python manage.py migrate` para ejecutar las migraciones a la base de datos
8.  `python manage.py runserver` para iniciar un servidor de desarrollo.

## Consideraciones finales.

- En la ruta `/trayectos` encontrará una vista muy simple para la creación de trayectos.
- En la ruta `/pasajeros` encontrará una vista muy simple para la creación de pasajeros.
- En la ruta `/choferes` encontrará una vista muy simple para la creación de choferes.
- En la ruta `/horarios` encontrará una vista muy simple para la creación de horarios.
- En la ruta `/boletos` encontrará una vista muy simple para la creación de boletos que es la relación entre un pasajero y un bus en uns fecha determinada.
- En la ruta `/buses` encontrará una vista muy simple para la creación de buses.
- En la ruta `/pasajeros_boletos` encontrará una vista muy simple para la creación de pasajeros asociandole un bus al momento de su creación.
  En la ruta `/buses_list` encontrará un GET de los buses con sus boletos.
