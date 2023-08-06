# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Joaquin
apellido:Carbonaro
---
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Fuego)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)
    0
    
    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    9
    
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario
    , si es impar, tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.(3)
    
    
    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
       # self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
       # self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
       # self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones =["Squirtle", "Psyduck", "Cloyster", "Charmander", "Drowzee", "Gyarados", "Squirtle", "Mewtwo", "Charizard", "Magikarp"]
        self.lista_poder_pokemones = [90, 150, 150, 95, 150, 90, 150, 150, 50, 103]
        self.lista_tipo_pokemones = ["agua", "psíquico", "agua", "fuego", "psíquico", "agua", "agua", "psíquico", "fuego", "agua"]

    def btn_mostrar_todos_on_click(self):
        #B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
        for i in range(0, len(self.lista_nombre_pokemones), 1):
            nombre = self.lista_nombre_pokemones[i]
            print(f"El nombre del pokemon es {nombre} y su posicion en la lista es {i}")

    
    def btn_mostrar_informe_1(self):
        #0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
        contador = 0
        for i in range (0, len(self.lista_tipo_pokemones), 1):
            tipo_elemento = self.lista_tipo_pokemones[i]
            if tipo_elemento == "fuego":
                 cant_puntos = self.lista_poder_pokemones[i] * 1.10
                 if cant_puntos > 100:
                     contador += 1
        
        print("Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10 porciento extra supere los 100 puntos: " + contador)
    
    def btn_mostrar_informe_2(self):
        #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.
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

        print ("El promedio de poder de todos los pokemones de tipo Psiquico es: " + promedio)


    def btn_mostrar_informe_3(self):
    #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
        bandera_primer = True
        minimo_psiquico = None
        
        # for i in range (0, len(self.lista_tipo_pokemones), 1):
        #     poder_ataque = self.lista_poder_pokemones[i]
        #     tipo_elemento = self.lista_tipo_pokemones[i]
        #     nombre = self.lista_nombre_pokemones[i]
        #     if tipo_elemento == "psíquico":
        #         if bandera_primer or poder_ataque < minimo:
        #             minimo = poder_ataque
        #             nombre_psiquico = nombre
        #             bandera_primer = False

        for i in range (len(self.lista_tipo_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            nombre = self.lista_nombre_pokemones[i]
            if tipo == "psíquico":
                if bandera_primer or (poder < minimo_psiquico or poder == minimo_psiquico):
                    minimo_psiquico = poder
                    bandera_primer = False
                    print(f"El nombre del pokemon Psiquico es {nombre} con el poder mas bajo que es {poder}")
            
        # for i in range (len(self.lista_tipo_pokemones)):
        #     poder = self.lista_poder_pokemones[i]
        #     if tipo == "psíquico" and poder == minimo_psiquico:
                    

    def btn_cargar_pokedex_on_click(self):
#       A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
#       Los datos que deberas pedir para los pokemones son:
#     * El nombre del pokemon
#     * El tipo de su elemento (Agua, Psiquico, Fuego)
#     * Poder de ataque (validar que sea mayor a 50 y menor a 200)
        for i in range(0, 10, 1):
            nombre = prompt("Pregunta", "Ingrese el nombre de  su pokemon: ")
            while nombre == None or nombre.isdigit():
                nombre = prompt("Pregunta", "Reingrese el nombre de  su pokemon: ")
            self.lista_nombre_pokemones.append(nombre)

            tipo_elemento = prompt("Pregunta", "Ingrese el tipo de su pokemon: (Agua, Psiquico, Fuego)")
            while (tipo_elemento == None or tipo_elemento.isdigit()) or (tipo_elemento != ("Agua") and tipo_elemento != ("Psiquico") and tipo_elemento != ("Fuego")):
                tipo_elemento = prompt("Pregunta","Reingrese el nombre de  su pokemon: ")
            self.lista_poder_pokemones.append(tipo_elemento)

            poder_ataque = prompt("Pregunta", "Ingrese el poder de su pokemon: ")
            poder_ataque = int(poder_ataque)
            while (tipo_elemento == None) or (poder_ataque < 50 or poder_ataque > 200):
                poder_ataque = prompt("Pregunta","Reingrese el poder de su pokemon: ")   
                poder_ataque = int(poder_ataque)
            self.lista_tipo_pokemones.append(poder_ataque)
        
            
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()