import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

#buscar una letra en lista
letra_buscar = prompt("","Ingrese la letra que quiere buscar")
for letra in palabra:
    if letra == letra_buscar:
        print("Letra encontrada")
        break

#agregar/quitar a una lista vacia 
lista_vacia.append(elemento)
lista_vacia.remove(elemento)



############### POSICION con indices ############### 

# 1 lista:
DOLAR = 541
for i in range(len(self.lista_transacciones)):
    transaccion_peso = self.lista_transacciones[i]
    transaccion_dolar = self.lista_transacciones[i] / DOLAR
    print(f"Numero de transaccion: {i} - monto en pesos: {transaccion_peso} - monto en dolares: {transaccion_dolar}")

# 3 listas:
print("Votantes de Massa:")
print("i Edad")
for i in range(len(self.lista_edades_massa)):
    votantes_massa = self.lista_edades_massa[i]
    print(i, votantes_massa)

print("Votantes de Milei:")
print("i Edad")
for i in range(len(self.lista_edades_milei)):
    votantes_milei = self.lista_edades_milei[i]
    print(i, votantes_milei)

print("Votantes de Larreta:")
print("i Edad")
for i in range(len(self.lista_edades_larreta)):
    votantes_larreta = self.lista_edades_larreta[i]
    print(i, votantes_larreta)



############### ejemplos con 1 lista = modelo examen ############### 



############### 0-BUSCAR MAYOR ############### 

#posicion/edad(contenido de la lista)/tipo(persona/marca)
#entre 2 listas:

edad_mayor = None
posicion_del_mayor = None
voto_realizado = None

for i in range(0,len(self.lista_edades_milei),1):
    if edad_mayor == None or self.lista_edades_milei[i] > edad_mayor:
        edad_mayor = self.lista_edades_milei[i]
        posicion_del_mayor = i
        voto_realizado = "Milei"

for i in range(0,len(self.lista_edades_massa),1):
    if edad_mayor == None or self.lista_edades_massa[i] > edad_mayor:
        edad_mayor = self.lista_edades_massa[i]
        posicion_del_mayor = i
        voto_realizado = "Massa"

if edad_mayor != None:
    print(posicion_del_mayor, edad_mayor, voto_realizado)
else:
    print("Listas vacias")



############### 2-PROMEDIO c/lista ############### 

acumulador_milei = 0
acumulador_larreta = 0

for edades in self.lista_edades_milei:
    acumulador_milei += edades
if len(self.lista_edades_milei) > 0: #NO HAY NEGATIVOS, sino != 0
    promedio_milei = acumulador_milei / len(self.lista_edades_milei)
else:
    promedio_milei = 0

for edades in self.lista_edades_larreta:
    acumulador_larreta += edades
if len(self.lista_edades_larreta) > 0: #NO HAY NEGATIVOS, sino != 0
    promedio_larreta = acumulador_larreta / len(self.lista_edades_larreta)
else:
    promedio_larreta = 0

print(f"El promedio de edades de los votantes de Milei es: {promedio_milei:.2f} y el de Larreta es: {promedio_larreta:.2f}")



############### 4-VALORES QUE SUPEREN EL PROMEDIO total ############### 

acumulador_edades_massa = 0
acumulador_edades_milei = 0
acumulador_edaes_larreta = 0

for edades in self.lista_edades_massa:
    acumulador_edades_massa += edades

for edades in self.lista_edades_milei:
    acumulador_edades_milei += edades

for edades in self.lista_edades_larreta:
    acumulador_edaes_larreta += edades

acumulador_total = acumulador_edades_massa + acumulador_edades_milei + acumulador_edaes_larreta
contador_total = len(self.lista_edades_massa) + len(self.lista_edades_milei) + len(self.lista_edades_larreta)

if contador_total > 0: #NO HAY NEGATIVOS, sino != 0
    promedio_total = acumulador_total / contador_total
else:
    promedio_total = 0

print(f"promedio total: {promedio_total:.2f}") #dato para verificacion

for edades in self.lista_edades_massa:
    if edades > promedio_total:
        print("La edad del votante de Massa que superan el promedio es: ", edades)

for edades in self.lista_edades_milei:
    if edades > promedio_total:
        print("La edad del votante de Milei que superan el promedio es: ", edades)

for edades in self.lista_edades_larreta:
    if edades > promedio_total:
        print("La edad del votante de Larreta que superan el promedio es: ", edades)



############### 6-PORCENTAJE de votos de cada participante ############### 

contador_votos_massa = len(self.lista_edades_massa)
contador_votos_milei = len(self.lista_edades_milei)
contador_votos_larreta = len(self.lista_edades_larreta)
contador_total = (contador_votos_larreta + contador_votos_massa + contador_votos_milei)

if contador_total != 0:
    porcentaje_votos_massa = (contador_votos_massa * 100) / contador_total 
    porcentaje_votos_milei = (contador_votos_milei * 100) / contador_total 
    porcentaje_votos_larreta = (contador_votos_larreta * 100) / contador_total 
else:
    porcentaje_votos_massa = 0
    porcentaje_votos_milei = 0
    porcentaje_votos_larreta = 0

mensaje = f"Porcentaje de votos de cada candidato\n"
mensaje += f"porcentaje Massa: {porcentaje_votos_massa:.2f}%\n"
mensaje += f"porcentaje Milei: {porcentaje_votos_milei:.2f}%\n"
mensaje += f"porcentaje Larreta: {porcentaje_votos_larreta:.2f}%"

print(mensaje)



############### 8-MAYOR CONTADOR comparando listas ############### 

contador_votos_massa = len(self.lista_edades_massa)
contador_votos_milei = len(self.lista_edades_milei)
contador_votos_larreta = len(self.lista_edades_larreta)

if contador_votos_massa > contador_votos_milei and contador_votos_massa > contador_votos_larreta:
    contador_mayor = f"El ganador de las elecciones es Massa con: {contador_votos_massa:.2f} votos"
elif contador_votos_milei > contador_votos_larreta:
    contador_mayor = f"El ganador de las elecciones es Milei con: {contador_votos_milei:.2f} votos"
else:
    contador_mayor = f"El ganador de las elecciones es Larreta con: {contador_votos_larreta:.2f} votos"

print(contador_mayor)



############### 9-MAYOR PROMEDIO comparando listas ############### 

acumulador_ford = 0
acumulador_volvo = 0
acumulador_fiat = 0

for kms in self.lista_ford_kms:
    acumulador_ford += kms
if len(self.lista_ford_kms) > 0: #NO HAY NEGATIVOS, sino != 0
    promedio_kms_ford = acumulador_ford / len(self.lista_ford_kms)
else:
    promedio_kms_ford = 0


for kms in self.lista_volvo_kms:
    acumulador_volvo += kms
if len(self.lista_volvo_kms) > 0: #NO HAY NEGATIVOS, sino != 0
    promedio_kms_volvo = acumulador_volvo / len(self.lista_volvo_kms)
else:
    promedio_kms_volvo = 0


for kms in self.lista_fiat_kms:
    acumulador_fiat += kms
if len(self.lista_fiat_kms) > 0: #NO HAY NEGATIVOS, sino != 0
    promedio_kms_fiat = acumulador_fiat / len(self.lista_fiat_kms)
else:
    promedio_kms_fiat = 0


if promedio_kms_ford > promedio_kms_volvo and promedio_kms_ford > promedio_kms_fiat:
    promedio_mayor = f"Ford tiene el mayor de los promedios de kilometros con: {promedio_kms_ford:.2f}"
elif promedio_kms_volvo > promedio_kms_fiat:
    promedio_mayor = f"Volvo tiene el mayor de los promedios de kilometros con: {promedio_kms_volvo:.2f}"
else:
    promedio_mayor = f"Fiat tiene el mayor de los promedios de kilometros con: {promedio_kms_fiat:.2f}"

print(promedio_mayor)



##########################################################################################
############### RECORRER 3 LISTAS (MIN con posibles iguales) ############### modelo youtube

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