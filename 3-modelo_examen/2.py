import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
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
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
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

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_transacciones = []


    def btn_agregar_on_click(self):
        USD_ARS = 541

        dinero_usuario = self.txt_dinero.get()
        tipo_divisa = self.combobox_divisa.get()

        if dinero_usuario == '' or dinero_usuario == '0':
            alert ('UTN', 'Ingrese un Monto valido')
        else: 
            dinero_usuario = float(dinero_usuario)
            self.txt_dinero.delete(0, 'end')

        if tipo_divisa == "USD":
            dinero_usuario = dinero_usuario * USD_ARS 
                
        self.lista_transacciones.append(dinero_usuario)

        alert ('UTN','Importe cargado correctamente')
    
    def btn_mostrar_on_click(self):
        #B) Al presionar el boton mostrar se deberan listar las transacciones en USD, en ARS y su posicion en la lista (por terminal) """

        USD_ARS = 541
        for i in range(len(self.lista_transacciones)):
            valor = self.lista_transacciones[i]
            cambio_ars_usd = valor / USD_ARS

            if valor > 0:
                mensaje_ars = f"Ingreso:{valor} en ARS"
                mensaje_usd = f" y {cambio_ars_usd} en USD"
            else:
                mensaje_ars = f"Egreso:{valor} en ARS"
                mensaje_usd = f"y {cambio_ars_usd} en USD"

            print(mensaje_ars, mensaje_usd, 'corresponde al indice', i, )

    def btn_informar_on_click(self):
        #4- Informar las transacciones que superan el promedio total (en ARS)
        #5- Informar las transacciones que NO superan el promedio total (en USD)
        USD_ARS = 541
        acumulador_transacciones = 0

        if len(self.lista_transacciones) > 0:

            for valor in self.lista_transacciones:
                acumulador_transacciones += valor
                
            promedio_transacciones = acumulador_transacciones / len(self.lista_transacciones)
                
            for valor_transacciones in self.lista_transacciones:
                if valor_transacciones > promedio_transacciones:
                    mensaje_promedio = '{0:.2f}ARS supera el valor promedio del total de las transacciones'.format(valor_transacciones)
                else:
                    cambio_ars_usd = valor_transacciones / USD_ARS
                    mensaje_promedio = '{0:.4f}USD no supera valor promedio del total de las transacciones'.format(cambio_ars_usd)

                alert("promedio", mensaje_promedio)
        else:
            alert("utn", 'Se requiere el ingreso de datos para realizar el informe')

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
