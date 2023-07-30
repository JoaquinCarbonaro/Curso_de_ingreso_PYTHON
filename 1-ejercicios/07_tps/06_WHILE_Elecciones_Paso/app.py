'''
nombre:Joaquin
apellido:Carbonaro
---
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        candidato_mas_votos = None
        candidato_menos_votos = None
        edad_candidato_menos_votos = None
        total_votos = 0
        total_edades = 0
        cantidad_candidatos = 0

        while True:
            respuesta = question("TP 06", "¿Desea cargar datos de un candidato?")
            if respuesta == False:
                break
            
            nombre = prompt("TP 06", "Ingrese su nombre: ")
            while nombre == None or nombre.isdigit():
                nombre = prompt("TP 06", "Ingrese su nombre: ")

            edad = prompt("TP 06", "Ingrese su edad: ")
            edad_int = int(edad)
            while edad_int <= 25:
                edad = prompt("TP 06", "Ingrese su edad: ")
                edad_int = int(edad)
            
            cantidad_votos = prompt("TP 06", "Ingrese la cantidad de votos: ")
            cantidad_votos_int = int(cantidad_votos)
            while cantidad_votos_int < 0:
                cantidad_votos_int = prompt("TP 06", "Ingrese la cantidad de votos: ")
                cantidad_votos_int = int(cantidad_votos)

            if candidato_mas_votos == None or cantidad_votos_int > candidato_mas_votos:
                candidato_mas_votos = cantidad_votos_int
                nombre_candidato_mas_votos = nombre

            if candidato_menos_votos == None or cantidad_votos_int < candidato_menos_votos:
                candidato_menos_votos = cantidad_votos_int
                nombre_candidato_menos_votos = nombre
                
                edad_candidato_menos_votos = edad
                edad_candidato_menos_votos_str = str(edad_candidato_menos_votos)
            
            total_votos += cantidad_votos_int
            total_votos_str = str(total_votos)
            
            total_edades += edad_int

            cantidad_candidatos += 1


        if cantidad_candidatos != 0:
            promedio_edades = total_edades / cantidad_candidatos
        else:
            promedio_edades = 0

        print("El candidato con más votos es: " + nombre_candidato_mas_votos)
        print("El candidato con menos votos es: " + nombre_candidato_menos_votos + " de " + edad_candidato_menos_votos_str + " años.")
        print("El promedio de edades de los candidatos es: " + "{0:.2f}".format(promedio_edades))
        print("Total de votos emitidos: " + total_votos_str)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
