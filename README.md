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


from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
result
