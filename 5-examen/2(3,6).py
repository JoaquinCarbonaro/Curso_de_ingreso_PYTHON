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

        nacionalidad  = self.combobox_nacionalidad.get()

        if edad < 16 or edad >  115 or nacionalidad == "Extranjero" or (nacionalidad == "Naturalizado" and edad < 18):
            alert(title="voto invalido", message="no puede votar")
        else:
            alert(title="habilitado", message="votante valido")
            voto = prompt(title="voto", prompt="a quien va dirigido el voto: Massa - Milei - Larreta")
            while voto is None or not (voto == "Massa" or voto == "Milei" or voto == "Larreta"):
                voto = prompt(title="voto", prompt="seleccione nuevamente a quien va dirigido el voto: Massa - Milei - Larreta")

            match voto:
                case "Massa":
                    self.lista_edades_massa.append(edad)
                case "Milei":
                    self.lista_edades_milei.append(edad)
                case "Larreta":
                    self.lista_edades_larreta.append(edad)
            
            alert(title="votante habilitado", message= "voto habilitado")


    def btn_mostrar_on_click(self):
        if len(self.lista_edades_larreta) != 0:
            print(f"votantes Larreta\nposicion edad ")
        for i in range(0, len(self.lista_edades_larreta),1):
            print(f"{i:3}{self.lista_edades_larreta[i]:9}")

        if len(self.lista_edades_milei) != 0:
            print(f"votantes milei\nposicion edad ")            
        for i in range(0, len(self.lista_edades_milei),1):
            print(f"votantes milei\nposicion edad ")
            print(f"{i:3}{self.lista_edades_milei[i]:9}")

        if len(self.lista_edades_massa) != 0:
            print(f"votantes massa\nposicion edad ")
        for i in range(0, len(self.lista_edades_massa),1):

            print(f"{i:3}{self.lista_edades_massa[i]:9}")

    def btn_informar_1_onclick(self): #6- Informar Porcentaje de votos de cada participante
        contador_votos_massa = len(self.lista_edades_massa)
        contador_votos_milei = len(self.lista_edades_milei)
        contador_votos_larreta = len(self.lista_edades_larreta)
        contador_total = (contador_votos_larreta + contador_votos_massa + contador_votos_milei)
        porcentaje_votos_massa = 0
        porcentaje_votos_milei = 0
        porcentaje_votos_larreta = 0

        if (contador_votos_larreta + contador_votos_massa + contador_votos_milei) != 0:
            porcentaje_votos_massa = contador_votos_massa / contador_total * 100
            porcentaje_votos_milei = contador_votos_milei / contador_total * 100
            porcentaje_votos_larreta = contador_votos_larreta / contador_total * 100

        mensaje = f"Porcentaje de votos de cada candidato\nporcentaje massa: %{porcentaje_votos_massa:.2f}\nporcentaje milei: %{porcentaje_votos_milei:.2f}\nporcentaje larreta: %{porcentaje_votos_larreta:.2f}"

        alert(title="porcentaje votos candidatos", message=mensaje)


    def btn_informar_2_onclick(self): #3- Informar Promedio de Edades De los votantes de Massa y Larreta
        acumulador_edades_larreta = 0
        acumulador_edades_massa = 0
        promedio_edades_massa = 0
        promedio_edades_larreta = 0
        votantes_larreta = len(self.lista_edades_larreta)
        votantes_massa = len(self.lista_edades_massa)

        for edad in self.lista_edades_massa:
            acumulador_edades_massa += edad
        
        if votantes_massa != 0:
            promedio_edades_massa = acumulador_edades_massa / votantes_massa

        mensaje = f"promedio de edades de los votantes de massa: {promedio_edades_massa:.2f}\n"

        for edad in self.lista_edades_larreta:
            acumulador_edades_larreta += edad
        
        if votantes_larreta != 0:
            promedio_edades_larreta = acumulador_edades_larreta / votantes_larreta

        mensaje += f"promedio de edades de los votantes de larreta: {promedio_edades_larreta:.2f}"

        alert(title="promedios", message= mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x400")
    app.mainloop()


