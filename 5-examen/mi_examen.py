import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Joaquin
apellido:Carbonaro
---
Enunciado:
Elecciones Presidenciales:
Se pide un programa que agrega las edades de los votantes en distintas listas dependiendo de la persona votada.
Ademas se realizaran informes sobre los datos cargados.

* Edad: Por Textbox 
* Nacionalidad: Por ComboBox ("Argentino", "Extranjero", "Naturalizado")
* Voto: Por prompt ("Massa", "Milei", "Larreta")

-La Edad minima de voto es 16 años para los Argentinos, 18 años para los Naturalizados y los Extranjeros no 
pueden votar.
-La Edad ingresada no debe superar los 115 años

A)  Al presionar el botón 'Votar' si la edad es valida y la persona no es extranjera se debera preguntar a quien 
va dirigido el voto y cargarlo en la lista correspondiente.

Si La persona no puede votar indicarlo por un Alert
Si la persona puede votar validar que el votante sea valido
Si se voto correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar los votos de cada participante con el siguiente formato:
(i = Indice)
Votantes de Massa:
i Edad
0 17
1 42
2 32
Votantes de Milei:
i Edad
0 25
1 22
2 32
Votantes de Larreta:
i Edad
0 16
1 23
2 45

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar 
        0- Informar Del mayor votante de Milei o Massa posicion y edad.
    1- Informar Del menor votante de Larreta o Milei posicion y edad.
    2- Informar Promedio de Edades De los votantes de Milei y Larreta
    3- Informar Promedio de Edades De los votantes de Massa y Larreta
    4- Informar las edades que superan el promedio total
    5- Informar las edades que NO superan el promedio total de edad
    6- Informar Porcentaje de votos de cada participante
    7- Informar la cantidad de votantes que NO superan el promedio total de edades
    8- Informar el ganador de las elecciones (Suponiendo que solo hay uno, El que mas votos tuvo).
        9- Indicar que candidato tiene el mayor promedio de edad entre sus votantes
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")

        self.txt_edad = customtkinter.CTkEntry(master=self, placeholder_text="Edad")
        self.txt_edad.grid(row=1, padx=20, pady=20)

        self.combobox_nacionalidad = customtkinter.CTkComboBox(master=self, values=["Argentino", "Extranjero", "Naturalizado"])
        self.combobox_nacionalidad.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_votar = customtkinter.CTkButton(master=self, text="Votar", command=self.btn_votar_on_click)
        self.btn_votar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_1= customtkinter.CTkButton(master=self, text="Informar 1", command=self.btn_informar_1_onclick)
        self.btn_informar_1.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")     

        self.btn_informar_2= customtkinter.CTkButton(master=self, text="Informar 2", command=self.btn_informar_2_onclick)
        self.btn_informar_2.grid(row=6, padx=20, pady=20, columnspan=2, sticky="nsew")    

        self.lista_edades_massa = []
        self.lista_edades_milei = []
        self.lista_edades_larreta = []


    def btn_votar_on_click(self):
        # Enunciado:
        # Elecciones Presidenciales:
        # Se pide un programa que agrega las edades de los votantes en distintas listas dependiendo de la persona votada.
        # Ademas se realizaran informes sobre los datos cargados.

        # * Edad: Por Textbox 
        # * Nacionalidad: Por ComboBox ("Argentino", "Extranjero", "Naturalizado")
        # * Voto: Por prompt ("Massa", "Milei", "Larreta")

        # -La Edad minima de voto es 16 años para los Argentinos, 18 años para los Naturalizados y los Extranjeros no 
        # pueden votar.
        # -La Edad ingresada no debe superar los 115 años

        # A)  Al presionar el botón 'Votar' si la edad es valida y la persona no es extranjera se debera preguntar a quien 
        # va dirigido el voto y cargarlo en la lista correspondiente.

        # Si La persona no puede votar indicarlo por un Alert
        # Si la persona puede votar validar que el votante sea valido
        # Si se voto correctamente indicarlo con un Alert

        # -- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

        edad = self.txt_edad.get()
        edad_int = int(edad)
        if (edad_int == None) or edad_int > 115:
            edad = alert("UTN", "Reingrese su edad: ")
        else:
            nacionalidad = self.combobox_nacionalidad.get()
            if nacionalidad == None or (nacionalidad != "Argentino" and nacionalidad != "Extranjero" and nacionalidad != "Naturalizado"):
                nacionalidad = prompt("UTN", "Reingrese nacionalidad su nacionalidad: (Argentino, Extranjero, Naturalizado)")

            if (nacionalidad == "Argentino" and edad_int >= 16) or (nacionalidad == "Naturalizado" and edad_int >= 18):
                voto = prompt("UTN","Ingrese a la persona que quiera votar: (Massa, Milei, Larreta)")
                if voto == None or (voto != "Massa" and voto != "Milei" and voto != "Larreta"):
                    voto = prompt("UTN","Reingrese a la persona que quiera votar: (Massa, Milei, Larreta)")
                alert("UTN","Usted voto correctamente")
                
                if voto == "Massa":
                    self.lista_edades_massa.append(edad_int)
                elif voto == "Milei":
                    self.lista_edades_milei.append(edad_int)
                else:
                    self.lista_edades_larreta.append(edad_int)
            else:
                alert("UTN","Usted NO puede votar")
            
            print(self.lista_edades_massa)
        



    
    def btn_mostrar_on_click(self):
        # B) Al presionar el boton mostrar se deberan listar los votos de cada participante con el siguiente formato:
        # (i = Indice)
        # Votantes de Massa:
        # i Edad
        # 0 17
        # 1 42
        # 2 32
        # Votantes de Milei:
        # i Edad
        # 0 25
        # 1 22
        # 2 32
        # Votantes de Larreta:
        # i Edad
        # 0 16
        # 1 23
        # 2 45

        mensaje ="Votantes de Massa: \n"
        mensaje +="i - Edad \n"

        for i in range(len(self.lista_edades_massa)):
            votantes_massa = self.lista_edades_massa[i]
            mensaje = (f"{i} - {votantes_massa:.2f}")
            print("Votantes de Massa: \ni - Edad \n" + mensaje)

        for i in range(len(self.lista_edades_milei)):
            votantes_milei = self.lista_edades_milei[i]
            mensaje = (f"{i} - {votantes_milei:.2f}")
            print("Votantes de Milei: \ni - Edad \n" + mensaje)

        for i in range(len(self.lista_edades_larreta)):
            votantes_larreta = self.lista_edades_larreta[i]
            mensaje = (f"{i} - {votantes_larreta:.2f}")
            print("Votantes de Larreta: \ni - Edad \n" + mensaje)
        
    

    def btn_informar_1_onclick(self):
        #0- Informar Del mayor votante de Milei o Massa posicion y edad.
        lista_mayor_votante = []
                
        for votantes in self.lista_edades_milei:
            lista_mayor_votante.append(votantes)
            
        for votantes in self.lista_edades_massa:
            lista_mayor_votante.append(votantes)
        
        #busco nro max en la nueva lista creada
        votante_maximo = None

        for votantes in lista_mayor_votante:
            if votante_maximo == None or votantes > votante_maximo:
                votante_maximo = votantes
        
        #comparo con cada lista para ver si aparece el nro max
        for i in range(len(self.lista_edades_milei)):
            if votante_maximo == self.lista_edades_milei[i]:
                print(f"En la posicion {i}, el votante mas grande es de Milei y tiene: {votante_maximo:.2f}")

        for i in range(len(self.lista_edades_massa)):
            if votante_maximo == self.lista_edades_massa[i]:
                print(f"En la posicion {i}, el votante mas grande es de Massa y tiene: {votante_maximo:.2f}")


    def btn_informar_2_onclick(self):
        #9- Indicar que candidato tiene el mayor promedio de edad entre sus votantes
        acumulador_votos_massa = 0
        acumulador_votos_milei = 0
        acumulador_votos_larreta = 0

        for votos in self.lista_edades_massa:
            acumulador_votos_massa += votos
        if contador_votos != 0:
            contador_votos = len(self.lista_edades_massa)
            promedio_votos_massa = acumulador_votos_massa / contador_votos
        else:
            promedio_votos_massa = 0

        for votos in self.lista_edades_milei:
            acumulador_votos_milei += votos
            if contador_votos != 0:
            contador_votos = len(self.lista_edades_milei)
            promedio_votos_milei = acumulador_votos_milei / contador_votos
        else:
            promedio_votos_milei = 0

        for votos in self.lista_edades_larreta:
            acumulador_votos_larreta += votos
            if contador_votos != 0:
            contador_votos = len(self.lista_edades_larreta)
            promedio_votos_larreta = acumulador_votos_larreta / contador_votos
        else:
            promedio_votos_larreta = 0

        if promedio_votos_massa > promedio_votos_milei > promedio_votos_larreta:
            print("El candidato que tiene el mayor promedio de edad entre sus votantes es: Massa")
        elif promedio_votos_milei > promedio_votos_massa > promedio_votos_larreta:
            print("El candidato que tiene el mayor promedio de edad entre sus votantes es: Milei")
        elif promedio_votos_larreta > promedio_votos_massa > promedio_votos_milei:
            print("El candidato que tiene el mayor promedio de edad entre sus votantes es: Larreta")
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x400")
    app.mainloop()

