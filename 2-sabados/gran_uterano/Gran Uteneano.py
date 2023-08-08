import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #A
        contador_femenino = 0
        acumulador_edad_femenina = 0
        #B
        contador_masculino_b = 0
        #C
        flag_primer_votante_gianni = False
        #D
        contador_votos_giovanni = 0
        contador_votos_gianni = 0
        contador_votos_facu = 0
        for a in range(100):
        
            #ingreso de nombre
            nombre = prompt("Votación", "Ingrese su nombre")
            for index in range(0, 100, 1):
                        # inicio  fin   pasos
                if nombre != "" and nombre != None:
                    break
                nombre = prompt("ERROR", "Reingrese su nombre")
            

            #ingreso de edad
            #edad = prompt("Votación", "Ingrese su edad. Debe ser mayor de 13 años")
            for index in range(0, 100, 1):
                edad = prompt("Votación", "Ingrese su edad. Debe ser mayor de 13 años")
                edad = int(edad)
                if edad > 13:                 
                    break

            
            #ingreso de genero
            for index in range(0, 100, 1):
                genero = prompt("Votacion", "Ingrese su género (masculino, femenino u otro)")
                if genero == "masculino" or genero == "femenino" or genero == "otro":
                    break
                


            #ingreso de votación
            for index in range(0, 100, 1):
                nominado = prompt("Votación", "Ingrese a quién va a votar (Giovanni, Gianni o Facundo)")
                if nominado == "Giovanni" or nominado == "Gianni" or nominado == "Facundo":
                    break

            #match separacion por genero
            match genero:
                case "femenino":
                    contador_femenino = contador_femenino + 1
                    acumulador_edad_femenina = acumulador_edad_femenina + edad
                case "masculino":
                    if (edad > 24 and edad < 41) and (nominado == "Giovanni" or nominado == "Facundo"):#nominado != "Gianni"
                        contador_masculino_b += 1
                case _:
                    pass
            match nominado:
                case "Giovanni":
                    contador_votos_giovanni += 1
                case "Gianni":
                    contador_votos_gianni += 1
                case _:
                    contador_votos_facu += 1
                    
                
            if nominado == "Gianni":
                if flag_primer_votante_gianni == False or edad < edad_votante_gianni_joven:
                    edad_votante_gianni_joven = edad
                    votante_gianni_joven = nombre
                    flag_primer_votante_gianni = True

            respuesta = question("Nominados", "Desea continuar?")
            if respuesta == False:
                break
        
        #Procesos
        #A
        if contador_femenino == 0:
            promedio_edad_femenino = 0
        else:
            promedio_edad_femenino = acumulador_edad_femenina / contador_femenino
        
        alert("Uteniano", promedio_edad_femenino)
        #B
        mensaje_b = f"Hubieron {contador_masculino_b} hombres que votaron a Giovanni o a Facundo"
        alert("Uteniano", mensaje_b)
        #C
        if flag_primer_votante_gianni != False:
            mensaje_c = f"El nombre del votante más joven que votó a Gianni es {votante_gianni_joven}"
        else:
            mensaje_c = "Nadie votó por Gianni"
        alert("Uteniano", mensaje_c)
        #D
        contador_votos_total = contador_votos_giovanni + contador_votos_gianni + contador_votos_facu
        porcentaje_giovanni = (contador_votos_giovanni * 100) / contador_votos_total
        porcentaje_gianni = (contador_votos_gianni * 100) / contador_votos_total
        porcentaje_facu = (contador_votos_facu * 100) / contador_votos_total
        mensaje_d = f"Hubieron {contador_votos_total} votos, el {porcentaje_giovanni} votó por Giovanni, el {porcentaje_gianni} votó Gianni y el {porcentaje_facu} votó por Facundo"
        alert("Uteniano", mensaje_d)
        #E
        if contador_votos_gianni > contador_votos_giovanni and contador_votos_gianni > contador_votos_facu:
            nombre_participante_eliminado = "Gianni"
        elif contador_votos_giovanni > contador_votos_facu:
            nombre_participante_eliminado = "Giovanni"
        else:
            nombre_participante_eliminado = "Facu"
        mensaje_e = f"El participante eliminado es... {nombre_participante_eliminado}"
        alert("Uteniano", mensaje_e)
