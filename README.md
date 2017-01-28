# SOAT processor

## Installing.

Requires python 3.5 or higher.

Clone the repo:
``` sh
$git clone https://github.com/jaconsta/soat_cnpx.git
$ cd soat_cnpx
```

Create a virtual environment.

``` sh
$ python -m venv env_name
$ source env_name activate
```

And install dependencies.

``` sh
$ pip install -r dependencies.txt
```

Go to the api folder and run the migration to the database.

``` sh
$ python manage.py migrate
```

Run the testing server
``` sh
$ python manage.py runserver
```

(Optional) Create the superuser
``` sh
$ python manage.py createsuperuser
```

And follow the command instructions.

Notes:

On windows test cases won't run because Aloe (the testing framework) is
not compatible with windows.

If you are on windows download the following packages from
[here](http://www.lfd.uci.edu/%7Egohlke/pythonlibs/):
  - [curses](http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses)
  - [psycopg2](http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg)

## Description.

SOAT

### 1. DESCRIPCIÓN

#### ¿Qué es el SOAT?

Es un seguro obligatorio para todos los vehículos (incluye motocicletas) que transiten por el territorio nacional.
Ampara los daños corporales que se causen a las personas en accidentes de tránsito.
Se incluyen los vehículos extranjeros que circulen por las carreteras del país, y sólo están exentos aquellos vehículos
que se movilicen por vías férreas y a la maquinaria agrícola, mientras que no hagan uso de la vía pública.

#### ¿Cuáles son las características principales del seguro?

Las características principales del seguro son:
 - Es un seguro de accidentes personales.
 - Los asegurados son las víctimas potenciales de accidentes de tránsito.
 - Cubre los daños corporales a las personas en accidente de tránsito.
 - Tiene incorporado coberturas en caso de muerte como consecuencia de un accidente de tránsito.
 - Es de cubrimiento universal, es decir, cubre a todas las víctimas que resulten en accidentes de tránsito.



### 2.  REQUERIMIENTOS FUNCIONALES

Se debe crear un sistema que permita la generación del seguro de SOAT, se debe seguir un proceso en donde se captura la
información del vehículo a asegurar asi como la información del tomador del seguro. Al final el usuario debe recibir en
su correo electrónico con el resumen de compra.

 - Como tomador puedo ingresar la placa del vehículo.

 - El sistema verifica si la placa tiene un SOAT asociado, en cuyo caso, informa al tomador que el vehículo ya está asegurado.

 - El nuevo seguro tendrá vigencia a partir del día de la compra ó del día siguiente a la fecha de vencimiento del del seguro actual (Si tiene un seguro activo).

 - Como tomador puedo ingresar datos del vehículo:
   - Clase (Lista).
   - Subtipo (numérico), representa Número de pasajeros, Cilindraje o Toneladas depende de la Clase del vehículo (​1)​.
   - Edad en años (numérico).
   - Número de pasajeros (numérico).
   - Cilindraje (numérico).
   - Toneladas (numérico).

   __Nota__: ​los campos​ ​Número de pasajeros, Cilindraje y Toneladas depende de la Clase del vehícul
 - El sistema deberá mostrar el resumen de compra:
   - El valor a pagar según los datos los datos del vehículo y de la tabla ​1​. Por ejemplo si la clase del vehículo es ​
   MOTO​ y el Subtipo es de ​100 c.c​, entonces deberá pagar $272.700 de valor  prima, más 50% de contribución Fosyga,
   más $1.610 de tasa RUNT para un total de ​$410.660.
   - Coberturas ofrecidas por el seguro así como el monto máximo que cubre cada una:
     - Muerte y gastos funerarios: 750 SMLDV
     - Gastos médicos: 800 SMLDV
     - Incapacidad permanente: 180 SMLDV
     - Gastos de transporte: 10 SMLDV
   - Fecha y hora de inicio de vigencia del seguro.
   - **+ ​Exportar en PDF el resumen de compra.**
 - Como tomador puedo ingresar mis datos personales:
   - Tipo de documento
   - Numero de documento
   - Nombres
   - Apellidos
   - Correo electrónico
   - Teléfono

   __Nota__:​ Si el usuario ha comprado anteriormente con la aseguradora estos campos se deben pre-cargar para que el tomador pueda confirmarlos y actualizarlos si es necesario.

 - Como tomador puedo pagar mi póliza, a través de un formulario:
   - Número de tarjeta de crédito
   - Nombre del titular de la tarjeta
   - Fecha de vencimiento de la tarjeta
   - Código de seguridad de la tarjeta (CVV)
   - Número de cuotas

   __Nota__:​ Todos los campos son requeridos y la fecha de vencimiento
   debe ser mayor o igual al día de compra.

 - El sistema debe enviar un correo con el resumen de la compra al tomador.
 - Como administrador puedo ver listado de pólizas vendidas
 - Como administrador puedo ver el detalle resumen de compra de una póliza.

(1) [Tabla de tarificación dada por Fasecolda​](http://www.fasecolda.com/files/1114/8406/4009/Tarifas_soat_2016C004-09.pdf)

### 3. REQUERIMIENTOS NO FUNCIONALES

- El código debe estar en un sistema de repositorio como Github,
Bitbucket o Gitlab.
- El repositorio debe contar con un archivo README que contenga las
 instrucciones de instalación y ejecución del proyecto.
- El proyecto debe contar con Unit testing.
- El sistema debe estar desplegado en una plataforma como Heroku en
donde se pueda acceder a través de una URL.
- Usar una base de datos como MySQL,  PostgreSQL, MongoDB o cualquier
otra.
- Exponer los servicios a través de una API RESTFul para las operaciones
CRUD.
- Usar un lenguaje de backend de libre elección (Ruby, Python, Nodejs,
Go, PHP).
- Usar frameworks javascript y CSS para la construcción del front-end.
