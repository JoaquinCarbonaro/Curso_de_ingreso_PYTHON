import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Joaquin
apellido:Carbonaro
---
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("Ejercicio 08", "Ingrese un numero: ")
        numero_int = int(numero)
        contador = 0

        for i in range (1, numero_int + 1, 1):
            if (numero_int % i == 0):
                contador += 1
            
        if (contador == 2):
            alert("Ejercicio 08", "Es Primo")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()