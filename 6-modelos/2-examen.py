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

B) Al presionar el boton mostrar se deberan listar los edad de cada participante con el siguiente formato:
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
    6- Informar Porcentaje de edad de cada participante
    7- Informar la cantidad de votantes que NO superan el promedio total de edades
    8- Informar el ganador de las elecciones (Suponiendo que solo hay uno, El que mas edad tuvo).
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

        self.btn_informar_0= customtkinter.CTkButton(master=self, text="Informar 0", command=self.btn_informar_0_onclick)
        self.btn_informar_0.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")     

        self.btn_informar_1= customtkinter.CTkButton(master=self, text="Informar 1", command=self.btn_informar_1_onclick)
        self.btn_informar_1.grid(row=6, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_2= customtkinter.CTkButton(master=self, text="Informar 2", command=self.btn_informar_2_onclick)
        self.btn_informar_2.grid(row=7, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_3= customtkinter.CTkButton(master=self, text="Informar 3", command=self.btn_informar_3_onclick)
        self.btn_informar_3.grid(row=8, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_4= customtkinter.CTkButton(master=self, text="Informar 4", command=self.btn_informar_4_onclick)
        self.btn_informar_4.grid(row=9, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_5= customtkinter.CTkButton(master=self, text="Informar 5", command=self.btn_informar_5_onclick)
        self.btn_informar_5.grid(row=10, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_6= customtkinter.CTkButton(master=self, text="Informar 6", command=self.btn_informar_6_onclick)
        self.btn_informar_6.grid(row=11, padx=20, pady=20, columnspan=2, sticky="nsew")   

        self.btn_informar_7= customtkinter.CTkButton(master=self, text="Informar 7", command=self.btn_informar_7_onclick)
        self.btn_informar_7.grid(row=12, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_8= customtkinter.CTkButton(master=self, text="Informar 8", command=self.btn_informar_8_onclick)
        self.btn_informar_8.grid(row=13, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_9= customtkinter.CTkButton(master=self, text="Informar 9", command=self.btn_informar_9_onclick)
        self.btn_informar_9.grid(row=14, padx=20, pady=20, columnspan=2, sticky="nsew")

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


        # validacion = while solo cuando es prompt / if funciona con combobox
        #.isdigit.() = valida enteros positivos
        #.lower() = valida aunque sea minuscula o mayuscula
        edad = self.txt_edad.get()
        nacionalidad = self.combobox_nacionalidad.get()

        if nacionalidad == "Extranjero":
            alert("Error","No puede votar por ser extranjero")
        elif edad.isdigit() == False or int(edad) < 16 or int(edad) > 115:
            alert("Error","No puede votar, debe ser de entre 16 y 115 años")
        elif nacionalidad == "Naturalizado" and int(edad) < 18:
            alert("Error","La edad de un naturalizado para votar debe ser +18")
        else:
            edad = int(edad)
            voto = prompt("Voto","Ingrese el voto: (Massa, Milei, Larreta)")

            while voto.lower() != "Massa" and voto.lower() != "Milei" and voto.lower() != "Larreta":
                voto = prompt("Voto","Ingrese el voto: (Massa, Milei, Larreta)")

            match voto:
                case "Massa":
                    self.lista_edades_massa.append(edad)
                case "Milei":
                    self.lista_edades_milei.append(edad)
                case "Larreta":
                    self.lista_edades_larreta.append(edad)

            alert("Correcto","Puede votar")

    
    def btn_mostrar_on_click(self):
        # B) Al presionar el boton mostrar se deberan listar los edad de cada participante con el siguiente formato:
        # (i = Indice)
        # Votantes de Massa:
        # i Edad
        # 0 17
        # 1 42
        # 2 32

        print("Votantes de Massa:")
        print("i Edad")
        for i in range(len(self.lista_edades_massa)):
            votantes_massa = self.lista_edades_massa[i]
            print(i, votantes_massa)

        print("Votantes de Milei:")
        print("i Edad")
        for i in range(len(self.lista_edades_milei)):
            votantes_milei = self.lista_edades_milei[i]
            print(i, votantes_milei)

        print("Votantes de Larreta:")
        print("i Edad")
        for i in range(len(self.lista_edades_larreta)):
            votantes_larreta = self.lista_edades_larreta[i]
            print(i, votantes_larreta)
        
    

    def btn_informar_0_onclick(self):
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

        ########################################################

        edad_mayor = None
        posicion_del_mayor = None
        voto_realizado = None

        for i in range(0,len(self.lista_edades_milei),1):
            if edad_mayor == None or self.lista_edades_milei[i] > edad_mayor:
                edad_mayor = self.lista_edades_milei[i]
                posicion_del_mayor = i
                voto_realizado = "Milei"
        
        for i in range(0,len(self.lista_edades_massa),1):
            if edad_mayor == None or self.lista_edades_massa[i] > edad_mayor:
                edad_mayor = self.lista_edades_massa[i]
                posicion_del_mayor = i
                voto_realizado = "Massa"

        if edad_mayor != None:
            print(posicion_del_mayor, edad_mayor, voto_realizado)
        else:
            print("Listas vacias")

    def btn_informar_1_onclick(self):
        pass

    def btn_informar_2_onclick(self):
        pass        

    def btn_informar_3_onclick(self):
        pass

    def btn_informar_4_onclick(self):
        pass

    def btn_informar_5_onclick(self):
        pass

    def btn_informar_6_onclick(self):
        pass

    def btn_informar_7_onclick(self):
        pass

    def btn_informar_8_onclick(self):
        pass

    def btn_informar_9_onclick(self):
        #9- Indicar que candidato tiene el mayor promedio de edad entre sus votantes
        acumulador_edades_massa = 0
        acumulador_edades_milei = 0
        acumulador_edades_larreta = 0
        

        for edad in self.lista_edades_massa:
            acumulador_edades_massa += edad
        
        if len(self.lista_edades_massa) > 0:
            promedio_edades_massa = acumulador_edades_massa / len(self.lista_edades_massa)
        else:
            promedio_edades_massa = 0

        
        for edad in self.lista_edades_milei:
            acumulador_edades_milei += edad
        
        if len(self.lista_edades_milei) > 0:
            promedio_edades_milei = acumulador_edades_milei / len(self.lista_edades_milei)
        else:
            promedio_edades_milei = 0

        
        for edad in self.lista_edades_larreta:
            acumulador_edades_larreta += edad
        
        if len(self.lista_edades_larreta) > 0:
            promedio_edades_larreta = acumulador_edades_larreta / len(self.lista_edades_larreta)
        else:
            promedio_edades_larreta = 0


        if promedio_edades_massa > promedio_edades_milei and promedio_edades_massa > promedio_edades_larreta:
            promedio_mayor = f"Massa con {promedio_edades_massa}"
        elif promedio_edades_milei > promedio_edades_larreta:
            promedio_mayor = f"Millei con {promedio_edades_milei}"
        else:
            promedio_mayor = f"Larreta con {promedio_edades_larreta}"
            promedio_mayor = "Larreta con " + str(promedio_edades_larreta)
            promedio_mayor = "Larreta con {0}".format(promedio_edades_larreta)

        print(promedio_mayor)

if __name__ == "__main__":
    app = App()
    app.geometry("300x400")
    app.mainloop()

