import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

############### MATCH ############### 

match destino:
            case "Bariloche" | "Ushuaia":
                mensaje = "Frío"
            case _:
                mensaje = "Calor"

#anidado
match estacion:
            case "Verano":
                match destino:
                    case "Mar del plata" | "Cataratas":
                        mensaje = "Se viaja"
                    case _:
                        mensaje = "No se viaja"


############### IF ############### 

#anidado
if variable < variable:
    if variable < variable:
           
    else:
           
else:

#elif
if variable < variable:
       
elif variable < variable:
       
else:

#ejemplo
if(cantidad_int >= 6):
            descuento = 50
        elif(cantidad_int == 5):
            if(marca == "ArgentinaLuz"):
                descuento = 40
            else:
                descuento = 30
        elif(cantidad_int == 3):
            if(marca == "ArgentinaLuz"):
                descuento = 15
            elif(marca == "FelipeLamparas"):
                descuento = 10 
            else:
                descuento = 5
        else:
            descuento = 0

