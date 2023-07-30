import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

#Formas de salidas de texto:
variable = 0 #ej
mensaje = f'El nombre del candidato con más votos es: {variable},\n\
            El nombre del candidato con menos votos es: {variable}, y tiene {variable}\n\
            años de edad. El promedio de edades de los candidatos es: {variable},\n\
            y el total de votos emitidos es de {variable}'   
print(mensaje)

print("test{1}{0}".format("hola","chau"))


#Busqueda de maximos y minimos
es_primer_num = True
maximo = None
minimo = None

while True:
    numero_ingresado = prompt("Numero", "Ingrese un numero:")
    if numero_ingresado is None:
        break
    numero_ingresado = int(numero_ingresado)

    ######### OPCION 1 ##########
    if es_primer_num:
        maximo = numero_ingresado
        minimo = numero_ingresado
        es_primer_num = False

    elif numero_ingresado > maximo:
        maximo = numero_ingresado

    elif numero_ingresado < minimo:
        minimo = numero_ingresado

    ######### OPCION 2 ##########
    if es_primer_num or numero_ingresado > maximo:
        maximo = numero_ingresado

    if es_primer_num or numero_ingresado < minimo:
        minimo = numero_ingresado
        es_primer_num = False

    ######### OPCION 3 ##########
    if maximo == None or numero_ingresado > maximo:
        maximo = numero_ingresado

    if minimo == None or numero_ingresado < minimo:
        minimo = numero_ingresado


#validar que sea una palabra
bandera_numero = True
palabra = prompt("Mostrar","Ingrese una palabra: ")
 #ejemplo: Hola = [H],[o],[l],[a]

#cada elemento | iterable 
for letra in palabra:  
    if (letra < '0' or letra > '9') and (letra != '-' and letra != '.'):
        bandera_numero = False #Es palabra
        break

if bandera_numero: #Es un nro
    numero = float(palabra)
    alert("Numero",f"{numero}, es un numero")


#Validar un nro
while True:
    numero = prompt("Ingreso","Ingrese un numero: ")
    bandera_coma = False
    primero_digito = True
    bandera_valido = True

    if numero is None or numero == '':
        continue
    else:
        for digito in numero:
            if  digito == '-' and primero_digito == True and len(numero) > 1 or digito.isdigit():
                primero_digito = False
            elif  digito == '.' and bandera_coma == False:
                primero_digito = False
                bandera_coma = True
            else:
                bandera_valido = False
                print("No es un numero")
                break
        if bandera_valido:
            break

numero = float(numero)
print(numero)


# LISTAS
numero = 5
mi_lista = ['Hola','orden','l','a',1,'%',3.5,numero,True,',']
lista_vacia = []

print(mi_lista[2]) #imprime: "1"

palabra = "Pepe"
print(palabra[4]) #imprime: not range

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

#LEN
mi_lista = ['Hola','orden','l','a',1,'a','%',3.5,numero,True,',']
largo = len("Pepe")
print(largo) #responde: 4 (cuenta: 1,2,3,4)

for i in range(0,len(mi_lista),1):   #hasta la cantidad de elementos de mi lista 
    print(mi_lista[i])               #imprime toda la lista



#LISTAS (INGRESAR NRO MAYOR O IGUAL A 10, BUSACAR IMPARES y mostrar en nueva lista con una "," entre cada elemento )
lista_numeros_impares = []
numero = prompt("Numero", "Ingrese un numero: ")

while numero is None or not numero.isdigit() or int(numero) < 10:
    numero = prompt("Numero", "Reingrese un numero valido mayor o igual a 10: ")

numero = int(numero)

#para incluir hasta el ultimo lemento enel for:
    #1ra forma: for i in range(0,numero+1,1): (va creciente)
    #               if i % 2 == 1:  # impar
    #               alert("Mostrar", i)
for i in range(numero, 0, -1): #2da forma (va en decreciente)
    if i % 2 == 1:  # impar
        lista_numeros_impares.append(i)

# queremos lograr agregar una , luego de cada elemnto en la lista
# ej: lista = [5,9.80,"Pepe",'a',True,[1],None]
#        lista_numeros_impares.append(',')       #ESTA MAL

mensaje = ""
# bandera_primer_iteracion = True
# for elemento in lista_numeros_impares:
#     if bandera_primer_iteracion:
#         mensaje = str(elemento)
#         bandera_primer_iteracion = False
#     else:
#         mensaje += ', ' + str(elemento)       #ESTA MAL (queda coma tmb al final)

#tener en cuenta: lista = [1, 2, 3]  # len(lista) => 3
#tener en cuenta: lista[3]  # => error no existe indice (cuenta: 0,1,2)

for i in range(len(lista_numeros_impares)-1, 0, -1):    # len()-1 = valor de indice
    if i == len(lista_numeros_impares) - 1:             # i cambia pero (len(lista_numeros_impares)-1) siempre es el mismo
        mensaje = str(lista_numeros_impares[i]) #si es el primer elemento, solo agrego el elemento
    else:
        mensaje += ', ' + str(lista_numeros_impares[i]) #sino agrego una , y el elemento

#explicacion:i tomará los valores desde el índice del último elemento de (lens(lista_numeros_impares - 1)) hasta 
#            el índice 1 en orden descendente.
#              i= 4,3,2,1
#              len= 4 (range = 4,3,2,1)

alert("Informe", mensaje)

