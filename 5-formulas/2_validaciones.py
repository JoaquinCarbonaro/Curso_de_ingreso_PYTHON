import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


############### DATOS DE VALIDACIONES ###############

#validaciones ventanas emergentes

question:
            no = False
            si = True

prompt:
        ok(vacio) == "" / .isdigit()   
        cancel == None

#validaciones conectores logicos
letras_y_palabras = and
numeros = or

#validaciones
.isdigit() = valida enteros positivos / es redundante usar tmb == "" / se puede usar tmb == None
.lower() = valida aunque sea minuscula o mayuscula

#tipo de validaciones
while solo cuando es prompt

if funciona con combobox



############### COMBOBOX/PROMPT (3 listas)###############

edad = self.txt_edad.get()
nacionalidad = self.combobox_nacionalidad.get()

if nacionalidad == "Extranjero":
    alert("Error","No puede votar por ser extranjero")
elif edad.isdigit() == False or int(edad) < 16 or int(edad) > 115:
    alert("Error","No puede votar, debe ser de entre 16 y 115 años")
elif nacionalidad == "Naturalizado" and int(edad) < 18:
    alert("Error","La edad de un naturalizado para votar debe ser +18")
else:
    edad = int(edad)
    voto = prompt("Voto","Ingrese el voto: (Massa, Milei, Larreta)")

    while voto.lower() != "Massa" and voto.lower() != "Milei" and voto.lower() != "Larreta":
        voto = prompt("Voto","Ingrese el voto: (Massa, Milei, Larreta)")

    match voto:
        case "Massa":
            self.lista_edades_massa.append(edad)
        case "Milei":
            self.lista_edades_milei.append(edad)
        case "Larreta":
            self.lista_edades_larreta.append(edad)

    alert("Correcto","Puede votar")



############### PROMPT (3 listas)###############

while True:
    marca = prompt("UTN","Ingrese marca de vehiculo: (ford, volvo, fiat)")
    while (marca == None or marca.isdigit()) or (marca.lower() != "ford" and marca.lower() != "volvo"  and marca.lower() != "fiat"):
        marca = prompt("UTN","Reingrese marca de vehiculo: (ford, volvo, fiat)")

    kilometros = prompt("UTN","Ingrese los kilometros:")
    while kilometros == "" or kilometros == None or kilometros.isalpha() or int(kilometros) <= 0:
        kilometros = prompt("UTN","Reingrese los kilometros:")
    kilometros = int(kilometros)

    match marca:
        case 'ford':
            self.lista_ford_kms.append(kilometros)
        case 'volvo':
            self.lista_volvo_kms.append(kilometros)
        case 'fiat':
            self.lista_fiat_kms.append(kilometros)
    alert("UTN", "El vehículo se cargo correctamente")

    continuar = question(title="continuar", message="¿Desea continuar ingresando números?")
    if continuar:
        continue
    else:
        break  



############### -NUMERO (no ceros)- PROMPT (1 lista) ############### modelo parcial

numero = prompt("UTN","ingrese un nro:")
while numero is none or not numero.isdigit():
     numero = prompt("UTN","ingrese un nro:")
numero = int(numero)

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


############### -todo tipo- PROMPT ###############

#3 listas:
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

#sin listas:
POSTULANTES_TOTALES = 10
for i in range(0,POSTULANTES_TOTALES,1):
    
    nombre = prompt("UTN", "Ingrese nombre: ")
    while nombre == None or nombre.isdigit() or nombre == '':
        nombre = prompt("UTN", "Reingrese nombre")
        
    edad = prompt("UTN", "Ingrese edad: ")
    edad = int(edad)
    while edad == None or edad < 18:
        edad = prompt("UTN", "Reingrese edad, debe ser mayor de edad")
    edad = int(edad)
        
    genero = prompt("UTN", "Ingrese genero (F-M-NB): ")
    while genero == None or (genero != "F" and genero != "M" and genero != "NB"):
        genero = prompt("UTN", "Reingrese genero, debe ser F / M / NB")
        
    tecnologia = prompt("UTN", "Ingrese tecnologia (PYTHON - JS - ASP.NET): ")
    while tecnologia == None or (tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET"):
            tecnologia = prompt("UTN", "Reingrese tecnologia, debe ser PHYTHON / JS / ASP.NET")
        
    puesto = prompt("UTN", "Ingrese puesto (Jr - Ssr - Sr): ")
    while puesto == None or (puesto != "Jr" and puesto != "Ssr" and puesto != "Sr"):
        puesto = prompt("UTN", "Reingrese puesto, debe ser: Jr / Ssr / Sr ")




##########################################################################################
############### -NUMERO positivos- COMBOBOX (2 listas) ############### modelo youtube

#validar que sea una nro cuando ingresa palabras
precio_sin_iva_texto =  self.txt_precio_articulo.get()
iva_texto = self.combobox_iva.get()
contador_puntos = 0

if precio_sin_iva_texto != "":
    bandera_numero = True
    for letra in precio_sin_iva_texto:
        if (letra < '0' or letra > '9') and (letra != '.'): #si acepta negativos: (... and letra != '-')
            bandera_numero = False #Es una palabra
            break
    else:
        if letra == '.':
            contador_puntos += 1
else:
    bandera_numero = False

if bandera_numero != False and contador_puntos <= 1: #Es un nro
    precio_sin_iva_float = float(precio_sin_iva_texto)
    if iva_texto == "21":
        precio_con_iva_float = precio_sin_iva_float * 1.21
        self.lista_precios_21.append(precio_con_iva_float)
        alert(title="Exito", message="Se cargo correctamente el dato")
    elif iva_texto == "10.5":
        precio_con_iva_float = precio_sin_iva_float * 1.105
        self.lista_precios_105.append(precio_con_iva_float)
        alert(title="Exito", message="Se cargo correctamente el dato")
else:
    alert(title="Error", message="El valor no es valido")