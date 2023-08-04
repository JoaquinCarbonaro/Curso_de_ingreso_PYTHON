
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Diez
Nombre: Natalia
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
        USD = 541
        bandera_coma = False
        primero_digito = True
        bandera_valido = True

        lista_transacciones = self.lista_transacciones
        divisa = self.combobox_divisa.get()
        dinero = self.txt_dinero.get()

        if dinero == '' or dinero == "0": #se valida como string porque todavía no esta casteado como número float
            alert(title="Error", message="Debe llenar este campo con un número válido")
        else:
            for digito in dinero:
                if  digito == '-' and primero_digito == True and len(dinero) > 1:
                    primero_digito = False
                elif  digito == '.' and bandera_coma == False:
                    primero_digito = False
                    bandera_coma = True
                elif digito.isdigit():
                    primero_digito = False
                else:
                    bandera_valido = False
                    alert(title="Error", message="No es un número válido")
                    break

            if bandera_valido:
                dinero = float(dinero)
                if divisa == "USD": #sólo se evalúa si es USD para convertir los dolares a pesos
                    dinero = dinero * USD

                #Acá se suben los montos a la lista
                lista_transacciones.append(dinero) #después dilucido si es positivo o negativo cuando lo recorra
                alert(title="Correcto", message="Carga de datos realizada correctamente")
                print(dinero, divisa)

        
        
    def btn_mostrar_on_click(self):
        ARS = 0.0018484

        lista_transacciones = self.lista_transacciones
        
        
        for i in range (0, len(lista_transacciones),1):
            dinero_ARS = lista_transacciones[i] #creo una variable para llamar a cada elemento de la lista
            dinero_USD = dinero_ARS * ARS #convierto los pesos a dolares
            print(f"{i} ARS {dinero_ARS:.2f}, USD: {dinero_USD:.2f}") #imprimo el valor de cada elemento en ARS y en USD
            

    # 2- Promedio de dinero ingresado (mostrarlo en ARS) LISTO
    # 7- Informar la cantidad de transacciones que NO superan el promedio total

    def btn_informar_on_click(self):
        acumulador_dinero_ingresado_ARS = 0
        lista_transacciones = self.lista_transacciones
        cantidad_transacciones = len(lista_transacciones) #creo una variable con el largo de la lista, porque la reutilizo
        acumulador_egreso_ARS = 0
        acumulador_ingreso_ARS = 0
        contador_operaciones_ingreso = 0
        contador_transaccion_no_supera_promedio_total = 0

        """ 2- Promedio de dinero ingresado (mostrarlo en ARS) LISTO
        7- Informar la cantidad de transacciones que NO superan el promedio total """

        for i in range(0, cantidad_transacciones, 1):
            dinero_ARS = lista_transacciones[i] #creo nuevamente una variable guardando los valores de la lista
            if dinero_ARS > 0: #si el monto de la lista es positivo
                acumulador_ingreso_ARS += dinero_ARS #guardo el monto en un acumulador
                contador_operaciones_ingreso += 1 #guardo la cantidad de operaciones de ingreso
            elif dinero_ARS < 0:
                acumulador_egreso_ARS += dinero_ARS 
        
        promedio_ingresos = acumulador_ingreso_ARS / contador_operaciones_ingreso #saco el promedio sólo de ingresos
        ingresos_menos_egresos = acumulador_ingreso_ARS + acumulador_egreso_ARS #resto ingresos - egresos (se suman porque los egresos son negativos)
        promedio_total = ingresos_menos_egresos / cantidad_transacciones #saco el promedio total de todas las transacciones
        

        for elemento in lista_transacciones: #recorro sólo los elementos de la lista, no necesito los índices
            if elemento < promedio_total: #si el valor del elemento de la lista es menor al promedio total
                contador_transaccion_no_supera_promedio_total += 1 #acumulo la cantidad de transacciones menores al promedio total

        mensaje_salida = f"Promedio de dinero ingresado: {promedio_ingresos:.2f}"
        mensaje_salida += f"\nCantidad de transacciones que NO superan el promedio total {contador_transaccion_no_supera_promedio_total}"
        print(mensaje_salida)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


