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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        while True:
            numero = prompt("TP 08", "Ingrese un número:")
            
            if numero == None:
                break
            else:
                numero = int(numero)
                self.lista.append(numero)
            

    def btn_mostrar_estadisticas_on_click(self):
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        minimo_negativo = None
        maximo_positivo = None

        for elemento in self.lista:
            if elemento < 0:
                acumulador_negativos += elemento
                contador_negativos += 1
                if minimo_negativo == None or elemento < minimo_negativo:
                    minimo_negativo = elemento
            elif elemento > 0:
                acumulador_positivos += elemento
                contador_positivos += 1
                if maximo_positivo == None or elemento > maximo_positivo:
                    maximo_positivo = elemento
            else:
                contador_ceros += 1 

        if contador_negativos > 0:
            promedio_negativos = acumulador_negativos / contador_negativos

        resultado = "Suma acumulada de los negativos: {}\n".format(acumulador_negativos)
        resultado += "Suma acumulada de los positivos: {}\n".format(acumulador_positivos)
        resultado += "Cantidad de números positivos ingresados: {}\n".format(contador_positivos)
        resultado += "Cantidad de números negativos ingresados: {}\n".format(contador_negativos)
        resultado += "Cantidad de ceros: {}\n".format(contador_ceros)
        resultado += "Mínimo de los negativos: {}\n".format(minimo_negativo)
        resultado += "Máximo de los positivos: {}\n".format(maximo_positivo)
        resultado += "Promedio de los negativos: {}\n".format(promedio_negativos)

        alert("TP 08", resultado)



        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
