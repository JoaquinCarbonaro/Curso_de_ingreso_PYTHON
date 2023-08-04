import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Joaquin
apellido:Carbonaro
---
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("SIMULACRO EXAMEN INGRESO")

        self.txt_precio_articulo = customtkinter.CTkEntry(master=self, placeholder_text="PRECIO")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_iva = customtkinter.CTkComboBox(master=self, values=["10.5", "21"])
        self.combobox_iva.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_precios_21= []
        self.lista_precios_105= []


    def btn_agregar_on_click(self):

        #validar que sea una nro cuando ingresa palabras
        precio_sin_iva_texto =  self.txt_precio_articulo.get()
        iva_texto = self.combobox_iva.get()
        contador_puntos = 0

        if precio_sin_iva_texto != "":
            bandera_numero = True
            for letra in precio_sin_iva_texto:
                if (letra < '0' or letra > '9') and (letra != '.'):
                    bandera_numero = False #Es una palabra
                    break
            else:
                if letra == '.':
                    contador_puntos += 1
        else:
            bandera_numero = False

        if bandera_numero != False and contador_puntos <= 1: #Es un nro
            precio_sin_iva_float = float(precio_sin_iva_texto)
            if iva_texto == "21":
                precio_con_iva_float = precio_sin_iva_float * 1.21
                self.lista_precios_21.append(precio_con_iva_float)
                alert(title="Exito", message="Se cargo correctamente el dato")
            elif iva_texto == "10.5":
                precio_con_iva_float = precio_sin_iva_float * 1.105
                self.lista_precios_105.append(precio_con_iva_float)
                alert(title="Exito", message="Se cargo correctamente el dato")
        else:
            alert(title="Error", message="El valor no es valido")
        
        # precio = self.txt_precio_articulo.get()
        # iva = self.combobox_iva.get()

        # if precio == '' or precio <= '0' or precio.isalpha():
        #     alert ('UTN', 'Ingrese un Monto valido')
        # else: 
        #     precio = float(precio)

        # if iva == "10.5":
        #     total = precio * 1.105
        #     self.lista_precios_105.append(total)
        # else:
        #     total = precio * 1.21
        #     self.lista_precios_21.append(total)
                
        # self.txt_precio_articulo.delete(0, 'end')
        # alert ('UTN','Importe cargado correctamente')
    
    def btn_mostrar_on_click(self):
        
        for i in range(len(self.lista_precios_105)):
            lista_105_sin_iva = self.lista_precios_105[i] / 1.105
            print(f"En la posicion {i}, el precio es: {lista_105_sin_iva:.2f} - IVA 10.5")

        for i in range(len(self.lista_precios_21)):
            lista_21_sin_iva = self.lista_precios_21[i] / 1.21
            print(f"En la posicion {i}, el precio es: {lista_21_sin_iva:.2f} - IVA 21")


    def btn_informar_on_click(self):
        
        ############### PUNTO 0 ############### 
        #valor y posicion frente al IVA del o los articulos sin IVA mas caros
        
        lista_articulos_105_21_sin_iva = []
            
        for precio_con_iva in self.lista_precios_105:
            precio_sin_iva = precio_con_iva / 1.105
            lista_articulos_105_21_sin_iva.append(precio_sin_iva)
            
        for precio_con_iva in self.lista_precios_21:
            precio_sin_iva = precio_con_iva / 1.21
            lista_articulos_105_21_sin_iva.append(precio_sin_iva)
        
        #busco nro max en la nueva lista creada
        precio_sin_iva_maximo = None

        for precio_sin_iva in lista_articulos_105_21_sin_iva:
            if precio_sin_iva_maximo == None or precio_sin_iva > precio_sin_iva_maximo:
                precio_sin_iva_maximo = precio_sin_iva
        
        #comparo con cada lista para ver si aparece el nro max
        for i in range(len(self.lista_precios_105)):
            lista_105_sin_iva = self.lista_precios_105[i] / 1.105
            if precio_sin_iva_maximo == precio_sin_iva:
                print(f"En la posicion {i}, el precio maximo es: {lista_105_sin_iva:.2f} - IVA 10.5")

        for i in range(len(self.lista_precios_21)):
            lista_21_sin_iva = self.lista_precios_21[i] / 1.105
            if precio_sin_iva_maximo == precio_sin_iva:
                print(f"En la posicion {i}, el precio maximo es: {lista_21_sin_iva:.2f} - IVA 10.5")


        ############### PUNTO 2 ###############
        # precio promedio sin IVA
 
        acumulador_precios_sin_iva = 0

        for precio_con_iva in self.lista_precios_105:
            acumulador_precios_sin_iva += precio_con_iva / 1.105

        for precio_con_iva in self.lista_precios_21:
            acumulador_precios_sin_iva += precio_con_iva / 1.21

        if contador_precios != 0:
            contador_precios = len(self.lista_precios_21) + len(self.lista_precios_105)
            promedio_precios_sin_iva = acumulador_precios_sin_iva / contador_precios
        else:
            promedio_precios_sin_iva = 0
        
        print("El promedio es: {0}".format(promedio_precios_sin_iva))


        ############### PUNTO 4 ############### 
        #valor y posicion frente al IVA del o los articulos que son mas caros que el promedio sin IVA

        acumulador_precios_sin_iva = 0

        for precio_con_iva in self.lista_precios_105:
            acumulador_precios_sin_iva += precio_con_iva / 1.105

        for precio_con_iva in self.lista_precios_21:
            acumulador_precios_sin_iva += precio_con_iva / 1.21

        if contador_precios != 0:
            contador_precios = len(self.lista_precios_21) + len(self.lista_precios_105)
            promedio_precios_sin_iva = acumulador_precios_sin_iva / contador_precios
        else:
            promedio_precios_sin_iva = 0
        
        for precio_con_iva in self.lista_precios_105:
            acumulador_precios_sin_iva += precio_con_iva / 1.105
            if precio_sin_iva > promedio_precios_sin_iva:
                print(f"En la posicion {i}, el precio maximo es: {lista_105_sin_iva:.2f} - IVA 10.5")

        for precio_con_iva in self.lista_precios_21:
            acumulador_precios_sin_iva += precio_con_iva / 1.21
            if precio_sin_iva > promedio_precios_sin_iva:
                print(f"En la posicion {i}, el precio maximo es: {lista_21_sin_iva:.2f} - IVA 21")


        ############### PUNTO 8 ############### 
        #valor y posicion frente al IVA del o los articulos cuyo valor se repitan en la lista que integran

        lista_sin_precios_repetidos = []
        #creamos lista no repetidos
        for precios_con_iva in self.lista_precios_105:
            if precios_con_iva not in lista_sin_precios_repetidos: #nro que no esta incluido en la lista
                lista_sin_precios_repetidos.append(precio_con_iva)

        #cuento cuantas veces aparecen los elementos unicos
        for precio_unico in lista_sin_precios_repetidos:
            cantidad_repetidos = 0
            for precios_con_iva in self.lista_precios_105:
                if precio_unico == precio_con_iva:
                    cantidad_repetidos += 1
            #el que aparezca mas de una vez, se imprime la posc que coincida en el for de lista original
            if cantidad_repetidos > 1:
                indice = 0
                for precios_con_iva in self.lista_precios_105:
                    if precio_unico == precio_con_iva:
                        print(f"En la posicion {indice}, el precio maximo es: {self.lista_precios_105[i]:.2f} - IVA 21")
                    cantidad_repetidos += 1


        ############### PUNTO 9 ###############
        #valor y posicion frente al IVA del o los articulos cuyo valor NO se repitan en la lista que integran
 
        lista_sin_precios_repetidos = []

        #creamos lista no repetidos
        for precios_con_iva in self.lista_precios_105:
            if precios_con_iva not in lista_sin_precios_repetidos: #nro que no esta incluido en la lista
                lista_sin_precios_repetidos.append(precio_con_iva)

        #cuento cuantas veces aparecen los elementos unicos
        for precio_unico in lista_sin_precios_repetidos:
            cantidad_repetidos = 0
            for precios_con_iva in self.lista_precios_105:
                if precio_unico == precio_con_iva:
                    cantidad_repetidos += 1
            #el que aparezca mas de una vez, se imprime la posc que coincida en el for de lista original
            if cantidad_repetidos == 1:
                indice = 0
                for precios_con_iva in self.lista_precios_105:
                    if precio_unico == precio_con_iva:
                        print(f"En la posicion {indice}, el precio maximo es: {self.lista_precios_105[i]:.2f} - IVA 21")
                    cantidad_repetidos += 1

        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()