import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


############### PORCENTAJES ############### 
float()

+ 10%
total = precio * 1.10

total = precio * incremento / 100
total = precio + incremento

- 10%
total = precio * 0.90

total = precio * descuento / 100
total = precio - descuento


resto = oper_A % oper_B == 0



############### PROMEDIO ############### 

if acumulador > 0:
    promedio = contador / acumulador
else:
    promedio = 0



############### MAX Y MIN ############### 

#Busqueda de maximos y minimos
bandera_primer = True
maximo = None
minimo = None

while True:
    numero_ingresado = prompt("Numero", "Ingrese un numero:")
    if numero_ingresado is None:
        break
    numero_ingresado = int(numero_ingresado)

    if bandera_primer or numero_ingresado > maximo:
        maximo = numero_ingresado

    if bandera_primer or numero_ingresado < minimo:
        minimo = numero_ingresado
        bandera_primer = False
print(f"El minimo es {minimo}")


#Busqueda de minimos comparando si hay mas de uno con mismo valor
bandera_primer = True
minimo = None
if bandera_primer or (numero_ingresado < minimo or numero_ingresado == minimo):
    minimo = numero_ingresado
    bandera_primer = False
    print(f"El minimo es {minimo}")



############### PRIMOS ############### 

numero = prompt("Ejercicio 08", "Ingrese un numero: ")
numero_int = int(numero)
contador = 0

for i in range (1, numero_int + 1, 1):
    if (numero_int % i == 0):
        contador += 1
    
if (contador == 2):
    alert("Ejercicio 08", "Es Primo")



############### NROS PARES ############### 

contador_par = 0
numero = prompt("Ejercicio 06", "Ingrese un numero: ")
numero_int = int(numero)

for i in range (1, numero_int + 1, 1):
    if (i % 2 == 0):
        contador_par += 1
        alert("Ejercicio 06", i)

alert("Ejercicio 06", f"La cantidad de numero pares son: {contador_par}")