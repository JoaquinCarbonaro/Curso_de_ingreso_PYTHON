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
        
        precio = self.txt_precio_articulo.get()
        iva = self.combobox_iva.get()

        if precio == '' or precio <= '0':
            alert ('UTN', 'Ingrese un Monto valido')
        else: 
            precio = float(precio)

        if iva == "10.5":
            total = precio * 1.105
            self.lista_precios_105.append(total)
        else:
            total = precio * 1.21
            self.lista_precios_21.append(total)
                
        self.txt_precio_articulo.delete(0, 'end')
        alert ('UTN','Importe cargado correctamente')
    
    def btn_mostrar_on_click(self):
        
        for i in range(0, len(self.lista_precios_105), 1):
            lista_105 = self.lista_precios_105[i]
            lista_105 /= 105
            print(f"Precio del articulo sin iva en la lista IVA 10.5%: {lista_105:.2f} y su posicion en la lista es {i}")

        for i in range(0, len(self.lista_precios_21), 1):
            lista_21 = self.lista_precios_21[i]
            lista_21 /= 21
            print(f"Precio del articulo sin iva en la lista IVA 21%: {lista_21:.2f} y su posicion en la lista es {i}")


    def btn_informar_on_click(self):
        #0:
        bandera_primer = True
        maximo_precio = None

        for i in range (len(self.lista_precios_105)):
            precio_105 = self.lista_precios_105[i]
            if bandera_primer or (precio_105 < maximo_precio or precio_105 == maximo_precio):
                maximo_precio_105 = precio_105
                bandera_primer = False
        
        for i in range (len(self.lista_precios_21)):
            precio_21 = self.lista_precios_21[i]
            if bandera_primer or (precio_21 < maximo_precio or precio_21 == maximo_precio):
                maximo_precio_21 = precio_21
                bandera_primer = False
        
        if maximo_precio_21 > maximo_precio_105:
            print(f"El precio mas caro es {maximo_precio_21} con el numero de indice: {i}")
        else:
            print(f"El precio mas caro es {maximo_precio_105} con el numero de indice: {i}")
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

