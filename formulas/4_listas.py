import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

############### POSICION con indices ############### 

#Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
for i in range(0, len(self.lista_nombre_pokemones), 1):
    nombre = self.lista_nombre_pokemones[i]
    print(f"El nombre del pokemon es {nombre} y su posicion en la lista es {i}")



############### RECORRER 3 LISTAS (MIN con posibles iguales) ############### 

#Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
bandera_primer = True
minimo_psiquico = None

for i in range (len(self.lista_tipo_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            nombre = self.lista_nombre_pokemones[i]
            if tipo == "psíquico":
                if bandera_primer or (poder < minimo_psiquico or poder == minimo_psiquico):
                    minimo_psiquico = poder
                    bandera_primer = False
                    print(f"El nombre del pokemon Psiquico es {nombre} con el poder mas bajo que es {poder}")



############### PROMEDIO (condicion 2 listas) ############### 

#el promedio de poder de todos los pokemones de tipo Psiquico.
contador = 0
acumulador = 0
for i in range (0, len(self.lista_tipo_pokemones), 1):
    tipo_elemento = self.lista_tipo_pokemones[i]
    if tipo_elemento == "psíquico":
        contador += 1
        acumulador += self.lista_poder_pokemones[i]

if acumulador > 0:
    promedio = contador / acumulador
else:
    promedio = 0


############### OTROS LISTAS ############### 

#buscar una letra en lista
letra_buscar = prompt("","Ingrese la letra que quiere buscar")
for letra in palabra:
    if letra == letra_buscar:
        print("Letra encontrada")
        break

#agregar/quitar a una lista vacia 
for elemento in mi_lista:
    if str(elemento).isalpha():
        lista_vacia.append(elemento)
        lista_vacia.remove(elemento)