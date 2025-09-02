#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugarDeResidencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarDeResidencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

print("Bienvenido a la Calculadora para encontrar el Radio de un ciruculo!!")

radio = float(input("Ingrese el radio del círculo: "))

area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

print("Bienvenido al conversor de segundos a horas!")

usuario = int(input("Ingrese la cantidad de segundos: "))

usuario = usuario / 3600

print(f"La cantidad de horas es: {usuario}")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un número: "))

print(f"La tabla de multiplicar de {numero} es:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Bienvenido a la calculadora basica!")

Usuario1 = int(input("Ingrese un número: "))

Usuario2 = int(input("Ingrese otro número: "))

print(f"La suma de {Usuario1} y {Usuario2} es: {Usuario1 + Usuario2}")
print(f"La resta de {Usuario1} y {Usuario2} es: {Usuario1 - Usuario2}")
print(f"La multiplicación de {Usuario1} y {Usuario2} es: {Usuario1 * Usuario2}")
print(f"La división de {Usuario1} y {Usuario2} es: {Usuario1 / Usuario2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

print("Bienvenido a la calculadora de IMC")

Altura = float(input("ingrese su altura en cm: "))
Peso = float(input("Ingrese su peso en Kg: "))


IMC = Peso / Altura ** 2

print(f"Su indice de masa corporal es de {IMC} kg")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

print("Bienvenido al conversor de grados Celsius a Fahrenheit!")

temperaturaC = int(input("Ingrese la temperatura en Celsius: "))

temperaturaC = 9/5 + 32

print(f"La temperatura en Fahrenheit es de: {temperaturaC} grados")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de
#dichos números.

print("Bienvenido! este es un programa para encontrar el promedio entre 3 numeros")

suma = 0
for i in range(3):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

promedio = suma / 3
print(f"El promedio entre los 3 números es: {promedio}")