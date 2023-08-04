import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Elecciones Presidenciales:
Se pide un programa que agrega las edades de los votantes en distintas listas dependiendo de la persona votada.
Ademas se realizaran informes sobre los datos cargados.

* Edad: Por Textbox 
* Nacionalidad: Por ComboBox ("Argentino", "Extranjero", "Naturalizado")
* Voto: Por prompt ("Massa", "Milei", "Larreta")

-La Edad minima de voto es 16 años para los Argentinos, 18 años para los Naturalizados y los Extranjeros no pueden votar.
-La Edad ingresada no debe superar los 115 años

A)  Al presionar el botón 'Votar' si la edad es valida y la persona no es extranjera se debera preguntar a quien va dirigido el voto y cargarlo
en la lista correspondiente.

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
        edad = self.txt_edad.get()
        edad = int(edad)
        nacionalidad = self.combobox_nacionalidad.get()

        if (nacionalidad == "Argentino" and (edad >= 16 and edad <= 115)) or (nacionalidad == "Naturalizado" and (edad >= 18 and edad <= 118)):
            candidato = prompt ("Votar" , "Por favor, escriba el nombre del candidato del que desea votar (Massa, Milei o Larreta)")
            while candidato != "Massa" and candidato != "Milei" and candidato != "Larreta":
                alert ("Error" , "Candidato no valido")
                candidato = prompt ("Reintento" , "Por favor, seleccione un candidato valido")
            match candidato:
                case "Massa":
                    self.lista_edades_massa.append(edad)
                   
                case "Milei":
                    self.lista_edades_milei.append(edad)
             
                case _:
                    self.lista_edades_larreta.append(edad)
            mensaje = "Carga exitosa"

        else:
            mensaje = "Usted no se encuentra habilitado para votar"

        alert ("Resultado" , mensaje)

    def btn_mostrar_on_click(self):
        print ("votantes de Massa\ni / edad")
        for i in range (len(self.lista_edades_massa)):
        
            print(f"{i} / {self.lista_edades_massa[i]}")
        print ("votantes de Milei\ni / edad")
        for j in range (len(self.lista_edades_milei)):
        
            print(f"{j} / {self.lista_edades_milei[j]}")
        print ("votantes de Larreta\ni / edad")
        for k in range (len(self.lista_edades_larreta)):
    
            print(f"{k} / {self.lista_edades_larreta[k]}")

    def btn_informar_1_onclick(self):
        cantidad_votantes_milei = len(self.lista_edades_milei) 
        edad_votantes_milei = 0
        cantidad_votantes_larreta = len(self.lista_edades_larreta)
        edad_votantes_larreta = 0

        for i in self.lista_edades_milei:
            edad_votantes_milei += i
        
        for j in self.lista_edades_larreta:
            edad_votantes_larreta += j

        if cantidad_votantes_milei != 0:
            promedio_edad_votantes_milei = edad_votantes_milei / cantidad_votantes_milei
            mensaje = f"El promedio de edad de los votantes de Milei es de {promedio_edad_votantes_milei} años\n"
        else:
            mensaje = "No hubieron votantes de Milei\n"

        if cantidad_votantes_larreta != 0:
            promedio_edad_votantes_larreta = edad_votantes_larreta / cantidad_votantes_larreta
            mensaje += f"El promedio de edad de los votantes de Larreta es de {promedio_edad_votantes_larreta} años"
        else:
            mensaje += "No hubieron votantes de Larreta"

        alert ("Promedio de edades" , mensaje)

    def btn_informar_2_onclick(self):

        votantes_totales = len(self.lista_edades_larreta) + len(self.lista_edades_massa) + len(self.lista_edades_milei)
        
        cantidad_votantes_menores_al_promedio = 0

        edad_total_de_votantes = 0
        
        for i in self.lista_edades_larreta:
            edad_total_de_votantes += i
        for j in self.lista_edades_massa:
            edad_total_de_votantes += j
        for k in self.lista_edades_milei:
            edad_total_de_votantes += k

        if votantes_totales != 0:
            promedio_edades = edad_total_de_votantes / votantes_totales

            for edad in self.lista_edades_larreta:
                if edad < promedio_edades:
                    cantidad_votantes_menores_al_promedio += 1
            for edad in self.lista_edades_massa:
                if edad < promedio_edades:
                    cantidad_votantes_menores_al_promedio += 1
            for edad in self.lista_edades_milei:
                if edad < promedio_edades:
                    cantidad_votantes_menores_al_promedio += 1
            mensaje = f"La cantidad de edades que no superan al promedio son de {cantidad_votantes_menores_al_promedio}"
            alert ("Promedio de edades" , mensaje)
        else:
            alert ("Error" , "No se cargo ninguna edad")



if __name__ == "__main__":
    app = App()
    app.geometry("300x400")
    app.mainloop()


