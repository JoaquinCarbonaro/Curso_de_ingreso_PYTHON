import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Joaquin
apellido:Carbonaro
---
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_divisores = 0
        numero = prompt("Ejercicio 07", "Ingrese un numero: ")
        numero_int = int(numero)

        for i in range (1, numero_int + 1, 1):
            if (numero_int % i == 0):
                contador_divisores += 1
                alert("Ejercicio 07", i)
        
        contador_divisores_str = str(contador_divisores)
        alert("Ejercicio 07", "La cantidad de divisores son: " + contador_divisores_str)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()