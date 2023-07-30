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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_neg = 0
        contador_neg = 0
        acumulador_pos = 0
        contador_pos = 0
        contador_ceros = 0

        while True:
            numero = prompt("Ejercicio 10", "Ingrese un número:")
            
            if numero == None:
                break
            
            numero_int = int(numero)

            if numero_int < 0:
                acumulador_neg += numero_int
                contador_neg += 1
            elif numero_int > 0:
                acumulador_pos += numero_int
                contador_pos += 1
            else:
                contador_ceros += 1

        diferencia = contador_pos - contador_neg

        alert("Ejercicio 10", "La suma acumulada de los negativos: " + str(acumulador_neg) + "\nLa suma acumulada de los positivos: " + str(acumulador_pos) + "\nCantidad de números positivos ingresados: " + str(contador_pos) + "\nCantidad de números negativos ingresados: " + str(contador_neg) + "\nCantidad de ceros: " + str(contador_ceros) + "\nDiferencia entre la cantidad de los números positivos ingresados y los negativos: " + str(diferencia))
                

            

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
