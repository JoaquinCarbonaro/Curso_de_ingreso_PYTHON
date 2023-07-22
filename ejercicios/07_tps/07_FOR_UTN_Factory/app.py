'''
nombre:Joaquin
apellido:Carbonaro
---
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        # Variables para almacenar los resultados
        cant_nb_edad_25_40_ssrs = 0
        nombre_postulante_jr_menor_edad = None
        edad_total_f = 0
        edad_total_m = 0
        edad_total_nb = 0
        cant_f = 0
        cant_m = 0
        cant_nb = 0
        cant_python = 0
        cant_js = 0
        cant_aspnet = 0

        # Bucle para ingresar los datos de los 10 postulantes
        for _ in range(10):
            nombre = input("Ingrese el nombre del postulante: ")

            while True:
                edad = int(input("Ingrese la edad del postulante (mayor de edad): "))
                if edad >= 18:
                    break
                else:
                    print("Edad inválida. Debe ser mayor de edad.")
            
            genero = input("Ingrese el género del postulante (F-M-NB): ").upper()

            tecnologia = input("Ingrese la tecnología en la que programa el postulante (PYTHON - JS - ASP.NET): ").upper()

            puesto = input("Ingrese el puesto al que se postula el postulante (Jr - Ssr - Sr): ").capitalize()

            # Punto a
            if genero == "NB" and (tecnologia == "JS" or tecnologia == "ASP.NET") and 25 <= edad <= 40 and puesto == "Ssr":
                cant_nb_edad_25_40_ssrs += 1

            # Punto b
            if puesto == "Jr" and (nombre_postulante_jr_menor_edad is None or edad < nombre_postulante_jr_menor_edad):
                nombre_postulante_jr_menor_edad = nombre

            # Punto c
            if genero == "F":
                edad_total_f += edad
                cant_f += 1
            elif genero == "M":
                edad_total_m += edad
                cant_m += 1
            elif genero == "NB":
                edad_total_nb += edad
                cant_nb += 1

            # Punto d
            if tecnologia == "PYTHON":
                cant_python += 1
            elif tecnologia == "JS":
                cant_js += 1
            elif tecnologia == "ASP.NET":
                cant_aspnet += 1

        # Punto c
        promedio_edad_f = edad_total_f / cant_f if cant_f > 0 else 0
        promedio_edad_m = edad_total_m / cant_m if cant_m > 0 else 0
        promedio_edad_nb = edad_total_nb / cant_nb if cant_nb > 0 else 0

        # Punto e
        total_postulantes = cant_f + cant_m + cant_nb
        porcentaje_f = (cant_f / total_postulantes) * 100
        porcentaje_m = (cant_m / total_postulantes) * 100
        porcentaje_nb = (cant_nb / total_postulantes) * 100

        # Mostrar los resultados
        print("a. Cantidad de postulantes de género no binario (NB) que programan en ASP.NET o JS y cuya edad está entre 25 y 40, y se han postulado para un puesto Ssr:", cant_nb_edad_25_40_ssrs)
        print("b. Nombre del postulante Jr con menor edad:", nombre_postulante_jr_menor_edad)
        print("c. Promedio de edades por género:")
        print("   - Femenino:", promedio_edad_f)
        print("   - Masculino:", promedio_edad_m)
        print("   - No binario:", promedio_edad_nb)
        print("d. Tecnología con más postulantes:", "PYTHON" if cant_python > cant_js and cant_python > cant_aspnet else "JS" if cant_js > cant_aspnet else "ASP.NET")
        print("e. Porcentaje de postulantes de cada género:")
        print("   - Femenino:", f"{porcentaje_f:.2f}%")
        print("   - Masculino:", f"{porcentaje_m:.2f}%")
        print("   - No binario:", f"{porcentaje_nb:.2f}%")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
