import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: marca de vehiculo (ford, volvo, fiat) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 
Ford
0 - 1000 km
1 - 2000 km
Volvo
0 - 1000 km
1 - 2000 km
Fiat
0 - 1000 km
1 - 2000 km
etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su marca de vehiculo.
    1- El menor kilometraje y su marca de vehiculo.
    2- Kilometraje promedio de los autos.
    3- La marca con mas autos
    4- La marca con menos autos
    5- Informar los kilometrajes que NO superan el promedio (total).
    6- Informar los kilometrajes que superan el promedio (total).
    7- Indicar el menor de los promedios de kilometros por marca.
    8- Indicar el mayor de los promedios de kilometros por marca.




'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("MODELO EXAMEN")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
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

        self.lista_ford_kms = [20,552,6]
        self.lista_volvo_kms = [855,225,22]
        self.lista_fiat_kms = [5,225,2255]

    def btn_agregar_on_click(self):
        # A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
        # Los datos a cargar de cada vehiculo son: marca de vehiculo (ford, volvo, fiat) y kilometros*.

        # * Todos los autos son usados.

        # -- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --   

        while True:
            marca = prompt("UTN","Ingrese marca de vehiculo: (ford, volvo, fiat)")
            while marca.lower() != "ford" and marca.lower() != "volvo"  and marca.lower() != "fiat":
                marca = prompt("UTN","Reingrese marca de vehiculo: (ford, volvo, fiat)")

            kilometros = prompt("UTN","Ingrese los kilometros:")
            while kilometros.isdigit() == False or kilometros == None or kilometros == '0':
                kilometros = prompt("UTN","Reingrese los kilometros:")
            kilometros = int(kilometros)

            continuar = question(title="continuar", message="¿Desea continuar ingresando números?")
            if continuar:
                continue
            else:
                break     
    
    def btn_mostrar_on_click(self):
        # B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje 
        # y su posicion en la lista.
        # Ejemplo: 
        # Ford
        # 0 - 1000 km
        # 1 - 2000 km
        # Volvo
        # 0 - 1000 km
        # 1 - 2000 km
        # Fiat
        # 0 - 1000 km
        # 1 - 2000 km
        # etc..

        print("Ford")
        for i in range(len(self.lista_ford_kms)):
            kms_ford = self.lista_ford_kms[i]
            print(i, "-", kms_ford, "km")
        
        print("Volvo")
        for i in range(len(self.lista_volvo_kms)):
            kms_volvo = self.lista_volvo_kms[i]
            print(i, "-", kms_volvo, "km")
        
        print("Fiat")
        for i in range(len(self.lista_fiat_kms)):
            kms_fiat = self.lista_fiat_kms[i]
            print(i, "-", kms_fiat, "km")
    
    def btn_informar_0_onclick(self):
        #0- El mayor kilometraje y su marca de vehiculo.

        kilometros_mayor = None
        marca_vehiculo = None

        for i in range(0,len(self.lista_ford_kms),1):
            if kilometros_mayor == None or self.lista_ford_kms[i] > kilometros_mayor:
                kilometros_mayor = self.lista_ford_kms[i]
                marca_vehiculo = "Ford"
        
        for i in range(0,len(self.lista_volvo_kms),1):
            if kilometros_mayor == None or self.lista_volvo_kms[i] > kilometros_mayor:
                kilometros_mayor = self.lista_volvo_kms[i]
                marca_vehiculo = "Volvo"
        
        for i in range(0,len(self.lista_fiat_kms),1):
            if kilometros_mayor == None or self.lista_fiat_kms[i] > kilometros_mayor:
                kilometros_mayor = self.lista_fiat_kms[i]
                marca_vehiculo = "Fiat"

        if kilometros_mayor != None:
            print("El mayor kilometraje es:", kilometros_mayor, "y su marca es:", marca_vehiculo)
        else:
            print("Listas vacias")


    def btn_informar_0_click(self):
       pass


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
        #8- Indicar el mayor de los promedios de kilometros por marca.
        
        acumulador_ford = 0
        acumulador_volvo = 0
        acumulador_fiat = 0
        

        for kms in self.lista_ford_kms:
            acumulador_ford += kms
        
        if len(self.lista_ford_kms) > 0:
            promedio_kms_ford = acumulador_ford / len(self.lista_ford_kms)
        else:
            promedio_kms_ford = 0

        
        for kms in self.lista_volvo_kms:
            acumulador_volvo += kms
        
        if len(self.lista_volvo_kms) > 0:
            promedio_kms_volvo = acumulador_volvo / len(self.lista_volvo_kms)
        else:
            promedio_kms_volvo = 0

        
        for kms in self.lista_fiat_kms:
            acumulador_fiat += kms
        
        if len(self.lista_fiat_kms) > 0:
            promedio_kms_fiat = acumulador_fiat / len(self.lista_fiat_kms)
        else:
            promedio_kms_fiat = 0


        if promedio_kms_ford > promedio_kms_volvo and promedio_kms_ford > promedio_kms_fiat:
            promedio_mayor = f"El mayor de los promedios de kilometros es de la marca Ford con: {promedio_kms_ford:.2f}"
        elif promedio_kms_volvo > promedio_kms_fiat:
            promedio_mayor = f"El mayor de los promedios de kilometros es de la marca Volvo con: {promedio_kms_volvo:.2f}"
        else:
            promedio_mayor = f"El mayor de los promedios de kilometros es de la marca Fiat con: {promedio_kms_fiat:.2f}"

        print(promedio_mayor)



if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()

