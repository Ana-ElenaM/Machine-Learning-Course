# Machine-Learning-Course
# Python

### Variables y tipos

#Guardar un int, un float, un string e imprimirlos por pantalla

#Guardar dos números, sumarlos e imprimirlos por pantalla

#Guardar dos strings con un espacio en el medio

#Asignar dos valores a la vez

### Listas

#Guardar una lista y otra con diferentes tiñpos e imprimir por pantalla, y comprobar el tipo de objeto

#Guardar valores en una lista usando append() e imprimir por pantalla

#Imprimir el valor de una posición solo

# iterar usando for una lista mylist y mostrar por pantalla los valores

#Guardar valores en una lista usando insert() e imprimir por pantalla

### Operadores

#divide 1 entre 2

#Haz la división entera ahora de 1 entre 2 # descartar decimales

#Calcula el resto de 10 entre 3 e imprime por pantalla
#Pista: usa %
remainder = 10%3
print(remainder)


#eleva 7 al cuadrado y 2 al cubo
squared = 7**2
cubed = 2**3
print(squared)
print(cubed)

helloworld = "hola" * 3
helloworld

#Concatena dos listas

### Formato de cadena (string)

El formato de string es útil para insertar variables en cadenas.

name = "Juan"
print(f"Hola, {name}!")

También puedes especificar la precisión con la que se mostrará.

a = 13.1415
print(f'{a:.2f}')
print(f'{a:.4f}')

### Condiciones

Las condiciones permiten ejecutar código solo si se cumplen ciertas circunstancias.

#Rellena la x con un valor que cumpla todas las condiciones
x = 2
print(x == 3) # imprime False
print(x != 3) # imprime True
print(x < 3) # imprime True
print(x >= 3) # imprime False

#Rellena las siguientes variables para entrar en los dos bucles a la vez
name = "Juan"
age = 23
if name == "Juan" and age == 23:
    print("Tu nombre es Juan y tienes 23 años.")

if name == "Juan" or name == "Rick":
    print("Tu nombre es Juan o Rick.")

name = "Juan"
if name in ["Juan", "Rick"]:
    print("Tu nombre es Juan o Rick.")

statement = False
another_statement = True
if statement is True:
    # hacer algo
    pass
elif another_statement is True: # else if (si no)
    # hacer otra cosa
    pass
else:
    # hacer otra cosa
    pass

### Bucles

Los bucles permiten ejecutar el mismo código hasta que se cumpla cierta condición.

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

for x in range(5):
    print(x)

for x in range(5,15,3):
    print(x)

count = 0
while count < 5:
    print(count)
    count += 1  # Esto es lo mismo que count = count + 1

Puedes salir de un bucle con la palabra *break*.

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

Puedes saltar al siguiente paso con la palabra *continue*.

for x in range(10):
    # Comprueba si x es par
    if x % 2 == 0:
        continue
    print(x)

### Funciones

Las funciones son una forma de dividir el código en bloques, permitiéndonos ordenarlo, hacerlo más legible, reutilizarlo y ahorrar tiempo. Las funciones también son importantes para definir interfaces para que los programadores compartan su código.

def my_function():
    print("¡Hola desde My Function!")

my_function()

def my_function_with_args(username, greeting):
    print(f"Hola, {username} , desde My Function!, te deseo {greeting}")

my_function_with_args("Juan", "buena suerte :)")
my_function_with_args("Juan", "mala suerte :(")

def sum_two_numbers(a, b):
    return a + b

result = sum_two_numbers(1,1)
result

### Diccionarios

Un diccionario es un tipo de dato similar a los arrays, pero funciona con claves y valores en vez de índices. Se puede acceder a cada valor almacenado en un diccionario usando una clave, que es cualquier tipo de objeto (una cadena, un número, una lista, etc.) en lugar de usar su índice para abordarlo.

phonebook = {}
phonebook["Juan"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
phonebook

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
phonebook

phonebook = {"Juan" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print(f"El número de teléfono de {name} es {number}")

phonebook = {
   "Juan" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["Juan"]
phonebook

## Avanzado (Opcional)

### Cadenas (Strings)

image = 'my-image_date.png'

image = image[:-4]
image

image = image.split('_')
image

name, date = image
name, date

print(name.split('-')[0])
print(name.split('-')[1])

image = ('_').join(image)
image

image = image + '.png'
image

### Generadores

Los generadores se utilizan para crear iteradores, pero con un enfoque diferente. Los generadores son funciones simples que devuelven un conjunto iterable de elementos, uno a uno, de una manera especial.

for i in range(10):
    if i % 2:
        print(i)

def odd_generator():
    for i in range(10):
        if i % 2:
            yield i

for i in odd_generator():
    print(i)

### Comprensión de listas

Las comprensiones de lista son herramientas muy poderosas que crean una nueva lista basada en otra lista, en una sola línea legible.

numbers = [1, 2, 3]
new_numbers = [i*2 for i in numbers]
new_numbers

También pueden usarse para generar diccionarios.

numbers = [1, 2, 3]
new_numbers = {i: i*2 for i in numbers}
new_numbers

### Tuplas

Las tuplas son similares a las lista pero son inmutables (número de elementos y valores fijos).

a = (1, 2, 3)
a

print(a[0])
print(a[1])
print(a[2])

for i in a:
    print(i)

### Funciones

def my_func(a, b, c):
    print(a + b + c)

my_func(1, 2, 3)

# valores predeterminados

def my_func(a, b, c=3):
    print(a + b + c)

my_func(1, 2)
my_func(1, 2, 4)

# dar valores a las variables de la función

def my_func(a, b, c):
    print(a + b + c)

my_func(a=1, b=2, c=3)

# devolver varios valores

def my_func(a, b, c):
    return a, b, c # devolver una tupla

my_func(1, 2, 3)

a, b, c = my_func(1, 2, 3)
print(a)
print(b)
print(c)

def my_func(a, b, c):
    return [a, b, c] # devolver una lista

my_func(1, 2, 3)

a, b, c = my_func(1, 2, 3)
print(a)
print(b)
print(c)

### Avanzado para iteradores

# iterar dos listas al mismo tiempo

a = [1, 2, 3]
b = [4, 5, 6]

for i, j in zip(a, b):
    print(i, j)

# obtener índice y valor

a = [10, 20, 30]

for i, j in enumerate(a):
    print(i, j)

### Funciones lambda

Una función lambda es una pequeña función anónima.

x = lambda a : a + 10
x(5)

x = lambda a, b : a * b
x(5, 6)

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

mydoubler(10)

mytripler = myfunc(3)

mytripler(10)

### Funciones map, filter y reduce

### FOR SPACEX EX.
## **Etapa 1: Obtencion de datos**

En esta práctica obtendrás los datos para predecir si un falcon 9 aterizará con éxito o no. Los datos serán recogidos mediante la API de SpaceX y nos aseguraremos de que siguen un formato adecuado para las fases siguientes. El siguiente es un ejemplo de un aterrizaje exitoso: 

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/landing\_1.gif)

Aquí puedes ver varios ejemplos de aterrizajes fallidos:

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/crash.gif)

La gran mayoría de aterrizajes fallidos son intencionados para la realización de diversos controles. Estos aterrizajes se llevan a cabo la mayoria en el oceano, veremos estadísticas al respecto.

## Objetivos

En esta práctica realizaras una GET request a la API de SpaceX. Tambien realizarás cierto data wrangling básico y limpieza de datos.

***

## Importación de librerias.

Nos importamos las siguientes librerías necesarias para el desarrollo de la práctica. 

import requests
import pandas as pd
import numpy as np
import datetime

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
#Las opciones anteriores aseguran que pandas muestre el df completo en jupyternotebooks

Realicemos ahora una petición GET a la API de SpaceX. La URL es la siguiente.

spacex_url="https://api.spacexdata.com/v4/launches/past"

* Usando la librería requests usa el método GET y pasale como argumento URL anterior, guardala en una variable `response`  y realiza el print de `response.content`

#INSERTA AQUÍ TU CÓDIGO
response = requests.get(spacex_url)
print(response.content)
#requests.TIPODEPETICIÓN(URL)

#print(x.status_code)

Si la petición ha sido realizada correctamente el resultado del print debería ser similar al siguiente:

```
b'[{"fairings":{"reused":false,"recovery_attempt":false,"recovered":false, ...
```
(Recomendamos cerrar el resultado del print después de revisarlo para que google collab no sufra.)

Nuestra variable `response` contiene una grandísima cantidad de información sobre los SpaceX pero vamos a intentar formatearla para poder ver de que se trata exactamente y que nos interesa.

### Parte 1: Obtén los datos mediante peticiones GET y crea un dataframe

Hemos observado que la variable `response` tiene forma de diccionario (como la mayoría de respuestas a peticiones GET). Una forma efectiva de formatear dichos datos es transformarlos en un JSON y posteriormente en un dataframe de python:

data=response.json()
data=pd.json_normalize(data)

*Utilizando el dataframe anterior muestra las 5 primeras filas*

from requests.api import head
#INSERTA AQUÍ TU CÓDIGO
data.head()

Observemos que la mayoría de datos interesantes no se muestran de forma explícita sino que son IDs. Estos IDs nos permiten obtener mas información haciendo pediciones GET a diferentes endpoints de la API.
Para mas infrmación: https://docs.spacexdata.com/

Revisando la documentación de la API nos hemos dado cuenta de que no son necesarias todas las columnas, por lo que vamos a reducir nuestro dataframe a lo crucial:

#Reescribe el dataframe para quedarnos solo con las columnas 'rocket', 'payloads','success', 'launchpad', 'cores', 'flight_number', 'date_utc'
#INSERTA AQUÍ TU CÓDIGO:
data = data[['rocket', 'payloads','success', 'launchpad', 'cores', 'flight_number', 'date_utc']]

# Algunos cohetes tienen mas de una carga 'payload' o 'core'. 
# Estos datos nos darán problemas en un futuro, entonces nos limitearemos a aquellos que solamente tienen un core o una carga (payload):
data = data[data['cores'].map(len)==1]
data = data[data['payloads'].map(len)==1]

# Otro problema que tenemos es que ahora tenemos listas de longitud 1. 
# Las listas de python no son especialmente compatibles con SQL por lo que lo solucionaremos sacando el valor de la lista:
data['cores'] = data['cores'].map(lambda x : x[0])
data['payloads'] = data['payloads'].map(lambda x : x[0])

# El formato de la fecha no es especialmete cómodo por lo que lo formatearemos:
data['date'] = pd.to_datetime(data['date_utc']).dt.date

Si revisamos `rocket, payload,launchpad y cores` son IDs, estos IDs nos permiten hacer peticiones a diferetes endpoints y obtener más información. La información para cada variable se encuentra en los siguientes links:

*   Para <code>rocket</code> https://github.com/r-spacex/SpaceX-API/blob/master/docs/rockets/v4/one.md . De aquí nos quedaremos la versión del cohete propulsor.

*   Para <code>payload</code> https://github.com/r-spacex/SpaceX-API/blob/master/docs/payloads/v4/one.md . De aquí guardaremos la carga, la masa de esta carga, la orbita a la que fue enviada y el cliente.

*   Para <code>launchpad</code> https://github.com/r-spacex/SpaceX-API/blob/master/docs/launchpads/v4/one.md . Guardamos la latitud, longitud y nombre de las diferentes plataformas de lanzamiento.

*   Para <code>cores</code> https://github.com/r-spacex/SpaceX-API/blob/master/docs/cores/v4/one.md . Gaurdamos diferentes variables del nucleo.

Los datos serán guardados en listas y estas listas las utilizaremos para crear una nuevo dataframe con todos los datos:

#Para rocket
BoosterVersion = [] 

#Para paylaod
PayloadMass = []
Payload = []
Orbit = []
Customers= []

#Para launchpad
LaunchSite = []
Longitude = []
Latitude = []

#Para core
Outcome = []
Flights = []
GridFins = []
Reused = []
Legs = []
LandingPad = []
Block = []
Mission_Outcome = []
ReusedCount = []
Serial = []

Para completar las listas anteriores nos definiremos una lista de funciones para facilitar la obtención de los datos.

Empecemos con los cohetes:

# DEFINICIÓN FUNCIÓN 1
def getBoosterVersion(data): #Definimos la función
    for x in data['rocket']: #Iteramos por cada fila de la columna rocket
       if x: #Comprobamos que no este vacía
        response = requests.get("https://api.spacexdata.com/v4/rockets/"+str(x)) #Realizamos la petición GET (Aplicamos str() para poder concatenar)
        response = response.json() #Transformamos la respuesta en un diccionario.
        nombre_cohete = response["name"]
        BoosterVersion.append(response['name']) #Añadimos a BoosterVersion el valor con key 'name'

De <code>launchpad</code> nos gustaría quedarnos con la longitud, la latitud y el nombre de la plataforma

# DEFINICIÓN FUNCIÓN 2
#INSERTA AQUI TU CÓDIGO
def getLaunchSite(data):
  for q in data["launchpad"]:
    if q:
      response1 = requests.get("https://api.spacexdata.com/v4/launchpads/"+str(q))
      response1 = response1.json()
      name_launchpad = response1["name"]
      LaunchSite.append(response1['name'])
      Longitude.append(response1["longitude"])
      Latitude.append(response1['latitude'])

#Definimos la función getLaunchSite que recibe con argumento data
#Iteramos por cada fila de la columna launchpad
#Comprobamos que no este vacía
#Realizamos la petición GET (Aplicamos str() para poder concatenar)
#Transformamos la respuesta en un diccionario.
#Añadimos a Longitude el valor con key 'longitude'
#Añadimos a Latitude el valor con key 'latitude'
#Añadimos a LaunchSite el valor con key 'name'

De <code>payload</code> nos gustaría obtener la carga, el peso de la carga, el cliente y la órbita a la que fué enviada.

# DEFINICIÓN FUNCIÓN 3
#INSERTA AQUI TU CÓDIGO
def getPayloadData(data):
  for z in data["payloads"]:
    if z:
      response2 = requests.get("https://api.spacexdata.com/v4/payloads/"+str(z))
      response2 = response2.json()
      name_payload = response2["name"]
      PayloadMass.append(response2['mass_kg'])
      Payload.append(response2["name"])
      Orbit.append(response2['orbit'])
      Customers.append(response2['customers'])

#Definimos la función getPayloadData
#Iteramos por cada fila de la columna payloads
#Comprobamos que no este vacía
#Realizamos la petición GET (Aplicamos str() para poder concatenar)
#Transformamos la respuesta en un diccionario.
#Añadimos a Payload el valor con key 'name'
#Añadimos a Customers el valor con key 'customers'
#Añadimos a PayloadMass el valor con key 'mass_kg'
#Añadimos a Orbit el valor con key 'orbit'

La función para completar los datos de `core` tiene una complicación extra por lo que la damos hecha:

# DEFINICIÓN FUNCIÓN 4
def getCoreData(data):
    for core in data['cores']:
            if core['core'] != None:
                response = requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
                Block.append(response['block'])
                ReusedCount.append(response['reuse_count'])
                Serial.append(response['serial'])
            else:
                Block.append(None)
                ReusedCount.append(None)
                Serial.append(None)
            Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))
            Flights.append(core['flight'])
            GridFins.append(core['gridfins'])
            Reused.append(core['reused'])
            Legs.append(core['legs'])
            LandingPad.append(core['landpad'])

Las funciones anteriores rellenan las listas vacías, veamoslo en práctica. *Revisa que la lista BoosterVersion esta vacía*

#INSERTA AQUI TU CÓDIGO
print(BoosterVersion)

*Llama ahora la función `getBoosterVersion`.* (No devuelve nada así que no hace falta asignarle una variable. Solo instanciamos la funcion.)

# LLAMADA A FUNCIÓN 1
#INSERTA AQUI TU CÓDIGO
getBoosterVersion(data)

*Muestra los primeros 5 valores de la lista `BoosterVersion`*

#INSERTA AQUI TU CÓDIGO
BoosterVersion[0:5]

*Aplica el resto de funciones:*
(No devuelven nada así que no hace falta asignarles una variable. Solo instanciamos a las funciones.)

# LLAMADA A FUNCIÓN 2
#INSERTA AQUI TU CÓDIGO
getLaunchSite(data)

# LLAMADA A FUNCIÓN 3
#INSERTA AQUI TU CÓDIGO
getPayloadData(data)

# LLAMADA A FUNCIÓN 4
#INSERTA AQUI TU CÓDIGO
getCoreData(data)

Finalmente creamos un dataframe desde las listas anteriores. Primero convirtámolos en un diccionario:

launch_dict = {'FlightNumber': list(data['flight_number']),
'Date': list(data['date']),
'BoosterVersion':BoosterVersion,
'PayloadMass':PayloadMass,
'Payload':Payload,
'Orbit':Orbit,
'LaunchSite':LaunchSite,
'LandingOutcome':Outcome,
'Flights':Flights,
'GridFins':GridFins,
'Reused':Reused,
'Legs':Legs,
'LandingPad':LandingPad,
'Block':Block,
'Customers': Customers,
'Mission_Outcome':list(data['success']),
'ReusedCount':ReusedCount,
'Serial':Serial,
'Longitude': Longitude,
'Latitude': Latitude}

Y ahora crea un dataframe de Pandas desde el diccionario. Llámalo `launch_data`

#INSERTA AQUI TU CÓDIGO

launch_data = pd.DataFrame(launch_dict)
print(launch_data) 

Finalmente, muestra las primeras 5 filas del dataframe.

#INSERTA AQUI TU CÓDIGO
launch_data[0:5]

### Parte 2: Filtra el dataframe para que solo incluya los lanzamientos de falcon 9

El falcon 9 es una versión considerablemente más nueva y efectiva que el faclon 1. Dado que nos interesan los datos recientes y a futuro vamos a *eliminar los lanzamientos de `Falcon 1` del fataframe launch_data y llama al nuevo dataframe `data_falcon9`. Muestra las primeras 5 filas.*

# INSERTA AQUÍ TU CÓDIGO

data_falcon9 = launch_data.loc[launch_data["BoosterVersion"] != "Falcon 1"]

data_falcon9.head()

Ahora que hemos eliminado los lanzamientos de Falcon 1 la columna FlightNumber está desajustada. Vamos a volver a ordenarla:

data_falcon9.FlightNumber = list(range(1, data_falcon9.shape[0]+1))  #usamos para renumerar la fila correspondiente a BoosterVersion
data_falcon9.head()

### Parte 3: Ajustes finales

Debajo podemos observar que nos faltan ciertos valores.

data_falcon9.isnull().sum()

* Lo óptimo sería no tener celdas vacías por lo que vamos a ver que podemos hacer para solucionar esta situación.
La columna <code>LandingPad</code> tiene valores `None`en los casos donde el cohete no tuvo intención de aterrizar por lo que no tenía ningún LandingPad asignado. 

* Por otro lado, los valores innexistentes de `PayloadMass` si se pueden completar. *En este caso utilizaras la función `.mean()` para calcular la media y `.replace()` para reemplzar los valores `np.nan`.* 

# INSERTA AQUI TU CÓDIGO

#  = np.nanmean(data_falcon9["PayloadMass"])
# replace(media_payloadmass) in data_falcon9 for "PayloadMass" == nan

media_payloadmass = data_falcon9['PayloadMass'].mean()
no_nulos = data_falcon9['PayloadMass'].replace(np.nan, media_payloadmass)
data_falcon9["PayloadMass"] = no_nulos
data_falcon9.head()
#data_falcon9.isnull().sum()

# Nueva sección

# Nueva sección

El número de celdas vacías en la columna <code>PayLoadMass</code> debería cambiar a 0.

Por último tenemos que la columna `Customers` es una lista, y como hemos comentado previamente, no se llevan especialmente bien con SQL. 
*Transforma esta lista en una string aplicando `.map(lambda x : ','.join(x))` a la columna y guardalo en la misma columna.*

#INSERTA AQUÍ TU CÓDIGO

*Ahora exporta el dataset en formato `.csv`  con `index=False` y llámalo `dataset_part_1.csv`. Descarga el archivo porque será necesario en la siguiente práctica.*

#INSERTA AQUÍ TU CÓDIGO
data_falcon9.to_csv("dataset_part_1.csv", index=False)

pd.read_csv("/content/dataset_part_1.csv")

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
result
