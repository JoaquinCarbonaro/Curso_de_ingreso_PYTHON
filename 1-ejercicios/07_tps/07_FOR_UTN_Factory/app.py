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
        cantidad_postulantes_nb_asp_js_edad_25_40_ssr = 0
        contador_postulantes_nb = 0
        contador_postulantes_f = 0
        contador_postulantes_m = 0
        acumulador_edades_nb = 0
        acumulador_edades_m = 0
        acumulador_edades_f = 0
        bandera_primer_jr = True
        postulante_jr_menor_nombre = None
        postulante_jr_menor_edad = None
        contador_postulantes_phyton = 0
        contador_postulantes_aspnet = 0
        contador_postulantes_js = 0
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
                
            # Punto a
            match genero:
                case "F":
                    contador_postulantes_f += 1
                    acumulador_edades_f += edad
                case 'M':
                    contador_postulantes_m +=1
                    acumulador_edades_m += edad
                case 'NB':
                    contador_postulantes_nb +=1
                    acumulador_edades_nb += edad
                    if (tecnologia == "ASP.NET" or tecnologia == "JS") and (edad >= 25 and edad <= 40) and puesto == "Ssr":
                        cantidad_postulantes_nb_asp_js_edad_25_40_ssr += 1
            
            match tecnologia:
                case "ASP.NET":
                    contador_postulantes_aspnet += 1
                case "JS":
                    contador_postulantes_js += 1
                case "PHYTON":
                    contador_postulantes_phyton += 1
            
            # Punto b
            if puesto == "Jr" and (bandera_primer_jr or edad < postulante_jr_menor_edad):
                    postulante_jr_menor_nombre = nombre
                    postulante_jr_menor_edad = edad
                    bandera_primer_jr = False

        # Punto c
        if contador_postulantes_f != 0:
            promedio_edades_f = acumulador_edades_f / contador_postulantes_f
        if contador_postulantes_m != 0: 
            promedio_edades_m = acumulador_edades_m / contador_postulantes_m
        if contador_postulantes_nb != 0: 
            promedio_edades_nb = acumulador_edades_nb / contador_postulantes_nb
            
        # Punto d
        if contador_postulantes_phyton > contador_postulantes_aspnet and contador_postulantes_phyton > contador_postulantes_js:
            tecnologia_mas_postulantes = "PHYTON"
        elif contador_postulantes_js > contador_postulantes_aspnet and contador_postulantes_js > contador_postulantes_phyton:
            tecnologia_mas_postulantes = "JS"
        else:
            tecnologia_mas_postulantes = "ASP.NET"
         
        # Punto e   
        porcentaje_postulantes_f = contador_postulantes_f * 100 / POSTULANTES_TOTALES
        porcentaje_postulantes_m = contador_postulantes_m * 100 / POSTULANTES_TOTALES
        porcentaje_postulantes_nb = contador_postulantes_nb * 100 / POSTULANTES_TOTALES


        print("a. Cantidad de postulantes de género no binario (NB) que programan en ASP.NET o JS y cuya edad está entre 25 y 40, y se han postulado para un puesto Ssr: " + str(cantidad_postulantes_nb_asp_js_edad_25_40_ssr))
        print("b. Nombre del postulante Jr con menor edad: " + str(postulante_jr_menor_nombre))
        print("c. Promedio de edades por género: \n- Femenino: " + str(promedio_edades_f) + "\n- Masculino: " + str(promedio_edades_m) + "\n- No binario: " + str(promedio_edades_nb))
        print("d. Tecnología con más postulantes: " + str(tecnologia_mas_postulantes))
        print("e. Porcentaje de postulantes de cada género: " + "\n- Femenino: " + f"{porcentaje_postulantes_f:.2f}%" + "\n- Masculino: " + f"{porcentaje_postulantes_m:.2f}%" + "\n- No binario: " + f"{porcentaje_postulantes_nb:.2f}%")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
