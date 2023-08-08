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
La Cueva De Fausto:
Se pide un programa que agrega los ingresos y egresos de dinero en dos divisas, dólares y pesos

A)  Al presionar el botón 'Agregar' se debera cargar el dinero (Positivo si es un ingreso, negativo si es un egreso),
el cual podra ser ingresado en ARS o en USD.

    El tipo de cambio indicado mediante una lista desplegable.

* Flotantes Distintos de 0

Los ingresos/egresos se guardaran en la "self.lista_transacciones" en ARS.

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar las transacciones en USD, en ARS y su posicion en la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo dinero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo dinero de su DNI Personal (Ej 4), y restarselo al dinero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al dinero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar
        0- Cantidad de dinero (en ARS) y posicion (indice) de la transaccion de mayor valor
    1- Cantidad de dinero (en ARS) y posicion (indice) de la transaccion de menor valor
        2- Promedio de dinero ingresado (mostrarlo en ARS)
    3- Promedio de dinero egresado (mostrarlo en USD)
        4- Informar las transacciones que superan el promedio total (en ARS)
    5- Informar las transacciones que NO superan el promedio total (en USD)
        6- Informar la cantidad de Transacciones que superan el promedio total
    7- Informar la cantidad de transacciones que NO superan el promedio total
        8- Indicar Si hubo mas ingresos o egresos
        9- Indicar Si hubo ganancia o perdida


1 ARS son 0,0018484 USD
1 USD son 541 ARS
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("SIMULACRO EXAMEN INGRESO")

        self.txt_dinero = customtkinter.CTkEntry(master=self, placeholder_text="DINERO")
        self.txt_dinero.grid(row=1, padx=20, pady=20)

        self.combobox_divisa = customtkinter.CTkComboBox(master=self, values=["ARS", "USD"])
        self.combobox_divisa.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_0= customtkinter.CTkButton(master=self, text="Informar 0", command=self.btn_informar_0_onclick)
        self.btn_informar_0.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")     

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

        self.lista_transacciones = []


    def btn_agregar_on_click(self):
        #A)  Al presionar el botón 'Agregar' se debera cargar el dinero (Positivo si es un ingreso, negativo si es un egreso),
        # el cual podra ser ingresado en ARS o en USD.

        # El tipo de cambio indicado mediante una lista desplegable.

        # * Flotantes Distintos de 0

        # Los ingresos/egresos se guardaran en la "self.lista_transacciones" en ARS.

        # Si existe error al validar indicarlo mediante un Alert
        # Si se cargo  correctamente indicarlo con un Alert

        # -- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

        DOLAR = 541
        dinero =  self.txt_dinero.get()
        divisa = self.combobox_divisa.get()
        
        if dinero == '' or dinero == '0':
            alert ('UTN', 'Ingrese un monto valido')
        else:
            dinero = float(dinero)
            alert(title="Exito", message="Se cargo correctamente el valor")
            if divisa == "ARS":
                self.lista_transacciones.append(dinero)
            elif divisa == "USD":
                dinero_de_usd_a_ars = dinero * DOLAR
                self.lista_transacciones.append(dinero_de_usd_a_ars)
            else:
                alert(title="Error", message="El valor no es valido")
         
        self.txt_dinero.delete(0,'end')
    
    def btn_mostrar_on_click(self):
        #B) Al presionar el boton mostrar se deberan listar las transacciones en USD, en ARS y su posicion 
        # en la lista (por terminal)
        
        DOLAR = 541

        for i in range(len(self.lista_transacciones)):
            transaccion_peso = self.lista_transacciones[i]
            transaccion_dolar = self.lista_transacciones[i] / DOLAR
            print(f"Numero de transaccion: {i} - monto en pesos: {transaccion_peso} - monto en dolares: {transaccion_dolar}")



    def btn_informar_0_onclick(self):
        #0- Cantidad de dinero (en ARS) y posicion (indice) de la transaccion de mayor valor
        
        bandera_primer = True
        maximo = None

        for i in range(len(self.lista_transacciones)):
            dinero = self.lista_transacciones[i]
            if bandera_primer or dinero > maximo:
                maximo = dinero
                posicion = i
                bandera_primer = False
        print(f"La transaccion de mayor valor es {maximo} y su posicion es: {posicion}")
    
        pass

    def btn_informar_2_onclick(self):
        #2- Promedio de dinero ingresado (mostrarlo en ARS)

        acumulador_dinero_ingresado = 0
        contador_dinero_ingresado = 0

        for dinero in self.lista_transacciones:
            if dinero > 0:
                acumulador_dinero_ingresado += dinero
                contador_dinero_ingresado += 1 

        if contador_dinero_ingresado > 0:
            promedio_dinero_ingresado = acumulador_dinero_ingresado / contador_dinero_ingresado
        else:
            promedio_dinero_ingresado = 0

        print(f"El promedio de dinero ingresado es: {promedio_dinero_ingresado:.2f}")
    

    def btn_informar_3_onclick(self):
        pass
    
    def btn_informar_4_onclick(self):
        #4- Informar las transacciones que superan el promedio total (en ARS)

        acumulador_transacciones = 0
        contador_transacciones = len(self.lista_transacciones)

        for dinero in self.lista_transacciones:
            acumulador_transacciones += dinero

        if contador_transacciones != 0:
            promedio_total = acumulador_transacciones / contador_transacciones
        else:
            promedio_total = 0

        print(f"promedio total: {promedio_total:.2f}") #dato para verificacion

        for dinero in self.lista_transacciones:
            if dinero > promedio_total:
                print(f"Transaccion que supera el promedio total: {dinero:.2f}")

    
    def btn_informar_5_onclick(self):
        pass
    
    def btn_informar_6_onclick(self):
        #6- Informar la cantidad de Transacciones que superan el promedio total

        acumulador_transacciones = 0
        contador_transacciones = len(self.lista_transacciones)
        contador_transaccion_mayor_promedio = 0

        for dinero in self.lista_transacciones:
            acumulador_transacciones += dinero

        if contador_transacciones != 0:
            promedio_total = acumulador_transacciones / contador_transacciones
        else:
            promedio_total = 0

        print(f"promedio total: {promedio_total:.2f}") #dato para verificacion

        for dinero in self.lista_transacciones:
            if dinero > promedio_total:
                contador_transaccion_mayor_promedio += 1 
                print(f"La cantidad de transacciones que supean el promedio son: {contador_transaccion_mayor_promedio}")
    
    def btn_informar_7_onclick(self):
        pass
    
    def btn_informar_8_onclick(self):
        #8- Indicar Si hubo mas ingresos o egresos
        
        contador_ingresos = 0
        contador_egresos = 0

        for dinero in self.lista_transacciones:
            if dinero > 0:
                contador_ingresos += 1
            else:
                contador_egresos += 1

        if contador_ingresos > contador_egresos:
            print("Hubo mas ingresos")
        else:
            print("Hubo mas egresos")

    
    def btn_informar_9_onclick(self):
        #9- Indicar Si hubo ganancia o perdida
        
        acumulador = 0

        for dinero in self.lista_transacciones:
            acumulador += dinero

        if acumulador > 0:
            print("Hubo ganancias")
        else:
            print("Hubo perdidas")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()