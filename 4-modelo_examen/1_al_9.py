import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Bianucci
Nombre: Juan Cruz

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

        divisa = self.combobox_divisa.get()
        transaccion = self.txt_dinero.get()

        if transaccion is None or transaccion.isalpha() or transaccion == '0' or transaccion == '':
            alert ('ERROR' , 'Valor no valido')
        else:
            transaccion = float(transaccion)
            if divisa == 'USD':
                transaccion = transaccion * 541
            self.lista_transacciones.append(transaccion)
            alert ('Carga exitosa' , 'La transaccion se registro exitosamente')
    
    def btn_mostrar_on_click(self):
        
        for i in range (len(self.lista_transacciones)):
            print (i)
            valor_en_USD = self.lista_transacciones[i] * 0.0018484
            print (f'{self.lista_transacciones[i]} ARS / {valor_en_USD} USD')
            

    def btn_informar_on_click(self):
        
        #Ejemplo de uso de max en lista para hallar el mayor valor y su indice
        # maximo = max(self.lista_transacciones)

        # for monto in range (len(self.lista_transacciones)):
            
        #     if maximo == self.lista_transacciones[monto]:
        #         print(f'el mayor monto es {maximo} y su indice es {monto}')


        #0 y 1
        # primer_monto = True
        # monto_menor = 0
        # monto_mayor = 0
        
        # for monto in range (len(self.lista_transacciones)):
        #     if primer_monto is True:
        #         monto_menor = self.lista_transacciones[monto]
        #         indice_menor = monto
        #         monto_mayor = self.lista_transacciones[monto]
        #         indice_mayor = monto
        #         primer_monto = False
        #     else:
        #         if self.lista_transacciones[monto] < monto_menor:
        #             monto_menor = self.lista_transacciones[monto]
        #             indice_menor = monto
        #         elif self.lista_transacciones[monto] > monto_mayor:
        #             monto_mayor = self.lista_transacciones[monto]
        #             indice_mayor = monto

        # mensaje = f"La menor transaccion es de {monto_menor} ARS, y su posicion en el indice es {indice_menor}\nLa mayor transaccion es de {monto_mayor} ARS, y su posicion en el indice es {indice_mayor}"

        # alert ("Montos maximos y minimos" , mensaje)
        
        #2 y 3
        # ingresos_totales = 0
        # valor_ingresos = 0
        # egresos_totales = 0
        # valor_egresos = 0

        # for transaccion in self.lista_transacciones:
        #     if transaccion > 0:
        #         ingresos_totales += 1
        #         valor_ingresos +=transaccion
        #     else:
        #         egresos_totales += 1
        #         valor_egresos += transaccion

        # if ingresos_totales != 0:
        #     promedio_ingresos = valor_ingresos / ingresos_totales
        #     mensaje1 = f"El promedio de ingresos fue de {promedio_ingresos} ARS"
        # else:
        #     mensaje1 = "No hubieron ingresos"

        # if egresos_totales != 0:
        #     promedio_egresos = (valor_egresos / egresos_totales) / 541
        #     mensaje2 = f"El promedio de egresos fue de {promedio_egresos} USD"
        # else:
        #     mensaje2 = "No hubieron egresos"

        # alert ("Promedios" , f"{mensaje1}\n{mensaje2}")


        #4 y 5
        # transacciones_totales = len(self.lista_transacciones)
        # suma_de_transacciones = 0
        # lista_montos_superiores_al_promedio = []
        # lista_montos_inferiores_al_promedio = []

        # if transacciones_totales == 0:
        #     alert ("Error" , "No se cargo ningun valor")
        # else:
        #     for transaccion in self.lista_transacciones:
        #         suma_de_transacciones += transaccion
        
        #         promedio_de_transacciones = suma_de_transacciones / transacciones_totales
        #         if transaccion > promedio_de_transacciones:
        #             lista_montos_superiores_al_promedio.append(transaccion)
        #         else:
        #             transaccion = transaccion / 541
        #             lista_montos_inferiores_al_promedio.append(transaccion)

        #     alert ("Informe" , f"Transacciones superiores al promedio en ARS: {lista_montos_superiores_al_promedio}\nTransacciones inferiores al promedio en USD: {lista_montos_inferiores_al_promedio}")
    

        #6 y 7
        # transacciones_totales = len(self.lista_transacciones)
        # suma_de_transacciones = 0
        # contador_superior_al_promedio = 0
        # contador_inferior_al_promedio = 0
        # mensaje = "No se realizaron transacciones"
        
        # for transaccion in self.lista_transacciones:
        #     suma_de_transacciones += transaccion
        
        # if transacciones_totales != 0:
        #     promedio_de_transacciones = suma_de_transacciones / transacciones_totales
        #     for monto in self.lista_transacciones:
        #         if monto > promedio_de_transacciones:
        #             contador_superior_al_promedio += 1
        #         else:
        #             contador_inferior_al_promedio += 1
            
        #     mensaje = "Se realizaron {0} transacciones superiores al promedio.\nSe realizaron {1} transacciones inferiores al promedio".format(contador_superior_al_promedio, contador_inferior_al_promedio)
            
        # alert ("Informe" , mensaje)

        #8
        # contador_ingresos = 0
        # contador_egresos = 0

        # for transaccion in self.lista_transacciones:
        #     if transaccion > 0:
        #         contador_ingresos += 1
        #     else:
        #         contador_egresos +=1
        
        # if contador_ingresos > contador_egresos:
        #     mensaje = "Hubieron mas ingresos que egresos"
        # elif contador_ingresos == contador_egresos:
        #     mensaje = "Hubo la misma cantidad de egresos que de egresos"
        # else:
        #     mensaje = "Hubieron mas egresos que ingresos"
        
        # alert ("Informe" , mensaje)


        #9
        # sumatoria = 0

        # for transaccion in self.lista_transacciones:
        #     sumatoria += transaccion

        # if sumatoria > 0:
        #     mensaje = "Hubo ganancia"
        # elif sumatoria == 0:
        #     mensaje = "No hubieron perdidas ni ganancias"
        # else:
        #     mensaje = "Hubo perdida"

        # alert ("Informe" , mensaje)
           
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

