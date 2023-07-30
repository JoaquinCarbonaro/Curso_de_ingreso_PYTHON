import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


############### DATOS DE VALIDACIONES ###############

#validaciones ventanas emergentes
question =  no = False
            si = True

prompt =  ok(vacio) == ''
          cancel == None

#validaciones conectores logicos
letras_y_palabras = and
numeros = or



############### PALABRA IF {ingreso prompt} ###############

bandera_numero = True
palabra = prompt("Mostrar","Ingrese una palabra: ")

for letra in palabra:  
    if (letra < '0' or letra > '9') and (letra != '-' and letra != '.'): #Si Es palabra
        bandera_numero = False 
        break

if bandera_numero: #si ES un nro
    numero = float(palabra)
    alert("Numero",f"{numero}, es un numero, reingrese una palabra")


############### NUMERO IF {ingreso combobox} ###############

USD_ARS = 541
dinero_usuario = self.txt_dinero.get()
tipo_divisa = self.combobox_divisa.get()

if dinero_usuario == '' or dinero_usuario == '0':
    alert ('UTN', 'Ingrese un Monto valido')
else: 
    dinero_usuario = float(dinero_usuario)
    self.txt_dinero.delete(0, 'end')

if tipo_divisa == "USD":
    dinero_usuario = dinero_usuario * USD_ARS 
        
self.lista_transacciones.append(dinero_usuario)

alert ('UTN','Importe cargado correctamente')



############### PALABRAS Y NUMEROS WHILE {ingrerso prompt} ###############

#combobox
estado_civil = prompt("TP 05", "Ingrese su estado civil: \"Soltero/a\", \"Casado/a\"")
while estado_civil != "Soltero/a" and estado_civil != "Casado/a" :
    estado_civil = prompt("TP 05", "Ingrese su estado civil: \"Soltero/a\", \"Casado/a\"")

#guardado en listas:
for i in range(0, 10, 1):
            nombre = prompt("Pregunta", "Ingrese el nombre de  su pokemon: ") #palabra cualquiera
            while nombre == None or nombre.isdigit():
                nombre = prompt("Pregunta", "Reingrese el nombre de  su pokemon: ")
            self.lista_nombre_pokemones.append(nombre)

            tipo_elemento = prompt("Pregunta", "Ingrese el tipo de su pokemon: (Agua, Psiquico, Fuego)") #palabra exacta
            while (tipo_elemento == None or tipo_elemento.isdigit()) or (tipo_elemento != ("Agua") and tipo_elemento != ("Psiquico") and tipo_elemento != ("Fuego")):
                tipo_elemento = prompt("Pregunta","Reingrese el nombre de  su pokemon: ")
            self.lista_poder_pokemones.append(tipo_elemento)

            poder_ataque = prompt("Pregunta", "Ingrese el poder de su pokemon: ") #numero dentro de valores
            poder_ataque = int(poder_ataque)
            while (tipo_elemento == None) or (poder_ataque < 50 or poder_ataque > 200):
                poder_ataque = prompt("Pregunta","Reingrese el poder de su pokemon: ")   
                poder_ataque = int(poder_ataque)
            self.lista_tipo_pokemones.append(poder_ataque)


############### NUMERO WHILE{ingreso prompt} COMPLEJO ###############

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

#se trabaja asi despues:
numero = float(numero)
print(numero)

if ingreso == 0:
            valido = False

        if valido:
            alert("Informe", "Dato ingresado correctamente")
            ingreso = float(ingreso)
            divisa = self.combobox_divisa.get()

            if divisa == "USD":
                ingreso = ingreso * CONVERTIR_EN_ARS
            
            self.lista_transacciones.append(ingreso)
        else: 
            alert("Error", "Error, el dato ingresado no es valido, debe ser un número y no puede ser 0")
