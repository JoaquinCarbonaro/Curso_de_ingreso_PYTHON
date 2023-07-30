import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''LORENZO BUERO
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
    0- Cantidad de dinero (en ARS) y posicion (indice) de la transaccion de mayor valor ++++++
    1- Cantidad de dinero (en ARS) y posicion (indice) de la transaccion de menor valor
    2- Promedio de dinero ingresado (mostrarlo en ARS) 
    3- Promedio de dinero egresado (mostrarlo en USD) 
    4- Informar las transacciones que superan el promedio total (en ARS)
    5- Informar las transacciones que NO superan el promedio total (en USD)
    6- Informar la cantidad de Transacciones que superan el promedio total
    7- Informar la cantidad de transacciones que NO superan el promedio total
    8- Indicar Si hubo mas ingresos o egresos
    9- Indicar Si hubo ganancia o perdida ++++++++++++++


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
        
        CONVERTIR_EN_ARS = 541
        #BANDERA_NEGATIVOS = False#esta de mas
        

        ingreso = self.txt_dinero.get()
        bandera_coma = False
        primero_digito = True
        valido = True

        if ingreso is None or ingreso == '':
            valido = False

        else:
            for digito in ingreso: # DESDE ACÁ
                if  digito == '-' and primero_digito == True and len(ingreso) > 1:
                    primero_digito = False

                elif  digito == '.' and bandera_coma == False:
                    primero_digito = False
                    bandera_coma = True

                elif digito.isdigit():
                    primero_digito = False
                    continue

                else:
                    valido = False
                    break #HASTA ACÁ, ES OPCIONAL
            
        if ingreso == 0:
            valido = False

        if valido:
            alert("Informe", "Dato ingresado correctamente")
            ingreso = float(ingreso)
            divisa = self.combobox_divisa.get()

            if divisa == "USD":
                ingreso = ingreso * CONVERTIR_EN_ARS
            
            self.lista_transacciones.append(ingreso)
        else: 
            alert("Error", "Error, el dato ingresado no es valido, debe ser un número y no puede ser 0")
            

    
    def btn_mostrar_on_click(self):

        CONVERTIR_EN_USD = 0.0018484

        for i in range(0, len(self.lista_transacciones), 1):
            transaccion_usd = self.lista_transacciones[i] * CONVERTIR_EN_USD

            mensaje_dolares = "{:.2f}".format(transaccion_usd)
            print(i) #indice
            print(self.lista_transacciones[i]) #mensaje en pesos
            print(mensaje_dolares)#mensaje en dolares


    def btn_informar_on_click(self):
        if len(self.txt_dinero) > 0:
            #0
            cont = 0
            mayor_transaccion = None
            #9
            acum_transacciones = 0
            
            for transaccion in self.lista_transacciones:
                if cont == 0 or mayor_transaccion < transaccion:
                    mayor_transaccion = transaccion
                    indice_mayor_transaccion = cont

                acum_transacciones += transaccion
                cont += 1
            
            #0
            mensaje = "La transacción de mayor valor fué de {0}$ ARS, está alojada en el índice {1}".format(mayor_transaccion, indice_mayor_transaccion)
            alert("Mayor transaccion", mensaje)
            #9
            if acum_transacciones > 0:
                alert("Buenas noticias", "Hubieron ganancias")
            elif acum_transacciones < 0:
                alert("Malas noticias", "Tuvimos perdidas")
            else:
                alert("Noticias", "No hubieron ganancias ni pérdidas")

        else:
            alert("Error", "La lista está vacía")



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


