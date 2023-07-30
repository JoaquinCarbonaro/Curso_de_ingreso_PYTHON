import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Joaquin Carbonaro DNI: 43.517.710
.
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

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_transacciones = []


    def btn_agregar_on_click(self):

        valor_dolar = 541

        dinero = self.txt_dinero.get()
        while dinero == 0 or dinero.isalpha():
            alert("Error", "Monto inválido.")
            break

        divisa = self.combobox_divisa.get()

        if divisa == "USD":  #Convertir de USD a ARS
            dinero *= valor_dolar
        elif divisa != "ARS":
            alert("Error", "Divisa inválida. Debe ser 'ARS' o 'USD'.")
        
        dinero = float(dinero)
        self.lista_transacciones.append(dinero)
        alert("Éxito", f"Transacción agregada correctamente: {dinero} ARS")
        self.txt_dinero.delete(0, 'end')
            
    
    def btn_mostrar_on_click(self):
        
        valor_dolar = 541
        contador = 0

        for i in self.lista_transacciones:
            monto_usd = (i / valor_dolar)
            monto_ars = i
            contador += 1
            print(f"Transacción {contador}: USD {monto_usd:.2f} - ARS {monto_ars:.2f}")

    def btn_informar_on_click(self):
        es_primer_num = True
        maximo = None
        contador = 0
        acumulador = 0

        for i in self.lista_transacciones:
            monto_ars = i
            contador += 1
            if es_primer_num or i > maximo:
                maximo = i
                posicion = contador
                es_primer_num = False
        
        print(f"Transacción de mayor valor: {monto_ars:.2f} ARS y su posisicion es: {posicion}")
        
        resultado = acumulador / contador
        if resultado > 0:
            mensaje = "Hubo ganancias"
        else:
            mensaje = "Hubo perdidas"
        
        print(mensaje)




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()