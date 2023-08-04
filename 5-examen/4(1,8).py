import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Alumna: Cuenca Clara

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
        TITULO = "Votaciones"
        edad_correcta = False

        edad = self.txt_edad.get()
        if edad is None or edad == "" or edad.isalpha() or int(edad) > 115:
            alert("ERROR" , "Ingrese su edad correctamente")
        else:
            edad = int(edad)
            edad_correcta = True

        nacionalidad = self.combobox_nacionalidad.get()
    
        if edad_correcta:
            voto = prompt(TITULO, "Ingrese su voto: Massa, Milei o Larreta")
            while voto != "Massa" and voto != "Milei" and voto != "Larreta":
                voto = prompt("ERROR", "Ingrese su voto correctamente: Massa, Milei o Larreta")

            if (nacionalidad == "Argentino" and edad > 15) or (nacionalidad == "Naturalizado" and edad > 17) or edad > 115:
                
                alert(TITULO, "El voto fue cargado correctamente")

                match voto:
                    case "Massa":
                        self.lista_edades_massa.append(edad)
                    case "Milei":
                        self.lista_edades_milei.append(edad)
                    case "Larreta":
                        self.lista_edades_larreta.append(edad)
            else:
                alert(TITULO , "No está autorizado a votar")

    
    def btn_mostrar_on_click(self):
        mensaje_edades = ""
        for i in range (0, len(self.lista_edades_massa),1):
            edad = self.lista_edades_massa[i]
            mensaje_edades += f"Votantes de Massa:\n{i} . {edad} años\n"

        for i in range (0, len(self.lista_edades_milei),1):
            edad = self.lista_edades_milei[i]
            mensaje_edades += f"Votantes de Milei:\n{i} . {edad} años\n"
        
        for i in range (0, len(self.lista_edades_larreta),1):
            edad = self.lista_edades_larreta[i]
            mensaje_edades +=f"Votantes de Larreta:\n{i} . {edad} años\n"
        print(mensaje_edades)

    def btn_informar_1_onclick(self):
        #1- Informar Del menor votante de Larreta o Milei posicion y edad.
        mensaje_informe_1 = "Menor votante de Larreta o Milei:\n"
        primer_iteracion = True

        if len(self.lista_edades_larreta) == 0 and len(self.lista_edades_milei) == 0:
            mensaje_informe_1 += "No se ingresaron votos para ninguno de los dos candidatos"

        else:
            for i in range (0, len(self.lista_edades_milei),1):
                edad = self.lista_edades_milei[i]
                if primer_iteracion or edad < edad_mas_baja:
                    edad_mas_baja = edad
                    primer_iteracion = False
            for i in range (0, len(self.lista_edades_larreta),1):
                edad = self.lista_edades_larreta[i]
                if  primer_iteracion or edad < edad_mas_baja:
                    edad_mas_baja = edad
            for i in range (0, len(self.lista_edades_milei),1):
                edad = self.lista_edades_milei[i]
                if edad == edad_mas_baja:
                    mensaje_informe_1 += f"{i}. {edad} años"

            for i in range (0, len(self.lista_edades_larreta),1):
                edad = self.lista_edades_larreta[i]
                if edad == edad_mas_baja:
                    mensaje_informe_1 += f"{i}. {edad} años"

        alert("Votaciones" , mensaje_informe_1)
            
    def btn_informar_2_onclick(self):
        #8- Informar el ganador de las elecciones (Suponiendo que solo hay uno, El que mas votos tuvo).
        contador_votos_milei = 0
        contador_votos_larreta = 0
        contador_votos_massa = 0
        lista_contadores = []
        primer_iteracion = True

        if len(self.lista_edades_larreta) == 0 and len(self.lista_edades_massa) == 0 and len(self.lista_edades_milei) == 0:
            mensaje_informe_2 = "No se ingresaron candidatos"

        else: 
            mensaje_informe_2 = "El ganador de las elecciones es:\n"

            for i in range (0, len(self.lista_edades_milei),1):
                contador_votos_milei += 1
            for i in range (0, len(self.lista_edades_larreta),1):
                contador_votos_larreta += 1
            for i in range (0, len(self.lista_edades_massa),1):
                contador_votos_massa += 1

            lista_contadores.append(contador_votos_larreta)
            lista_contadores.append(contador_votos_massa)
            lista_contadores.append(contador_votos_milei)

            for i in range (0,len(lista_contadores),1):
                contador = lista_contadores[i]
                if primer_iteracion or maximo_contador < contador:
                    maximo_contador = contador
                    primer_iteracion = False
        
            if contador_votos_larreta == maximo_contador:
                mensaje_informe_2 += "Larreta\n"
            if contador_votos_massa == maximo_contador:
                mensaje_informe_2 +=  "Massa\n"
            if contador_votos_milei == maximo_contador:
                mensaje_informe_2 += "Milei"
        
        alert("Votaciones" , mensaje_informe_2)



if __name__ == "__main__":
    app = App()
    app.geometry("300x400")
    app.mainloop()



