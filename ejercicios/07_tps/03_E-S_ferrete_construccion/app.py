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

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (V)Poste Quebracho Fino de 2.2 mts
    (F)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        quebracho_grueso = 0
        quebracho_grueso_ancho = 0
        quebracho_grueso_largo = 0

        largo = self.txt_largo.get()
        ancho = self.txt_ancho.get()

        largo_float = float(largo)
        ancho_float = float(ancho)

        area = largo_float * ancho_float
        perimetro = (largo_float + ancho_float) * 2

        mensaje_punto_a = "Los metros cuadrados del terreno son: {0:.2f} m2 y los metros lineales del perimetro son: {1:.2f}".format(area, perimetro)

        if largo_float > 4.8 or ancho_float > 4.8:
            quebracho_grueso = 4
            quebracho_grueso_ancho = ancho_float // 250 * 2
            quebracho_grueso_largo = largo_float // 250 * 2

        quebracho_grueso += quebracho_grueso_ancho + quebracho_grueso_largo
        
        mensaje_punto_b ="La cantidad de quebrachos necesarios para el terreno son: {0}".format(quebracho_grueso)

        espacio_tomado_largo = 2.4 * quebracho_grueso_largo / 2
        espacio_tomado_ancho = 2.4 * quebracho_grueso_ancho / 2

        
        ancho_espacio_disponible = ancho_float - espacio_tomado_ancho
        largo_espacio_disponible = largo_float - espacio_tomado_largo

        quebracho_fino_ancho = ancho_espacio_disponible // 12 * 2
        quebracho_fino_largo = largo_espacio_disponible // 12 * 2

        quebracho_fino = quebracho_fino_ancho + quebracho_fino_largo

        mensaje_punto_c = "La cantidad de quebracho fino necesario para el terreno son: {0}".format(quebracho_fino)

        espacio_tomado_largo += 2.2 * quebracho_fino_largo / 2
        espacio_tomado_largo += 2.2 * quebracho_fino_ancho / 2

        ancho_espacio_disponible = ancho_float - espacio_tomado_ancho
        largo_espacio_disponible = largo_float - espacio_tomado_largo

        varillas_ancho = ancho_espacio_disponible // 2 * 2
        varillas_largo = largo_espacio_disponible // 2 * 2

        varilla = varillas_ancho + varillas_largo

        mensaje_punto_d = "La cantidad de varillas necesarias son: {0}".format(varilla)

        alambre = perimetro * 7

        mensaje_punto_e = "La cantidad de alambre necesario es: {0:.2f} mts".format(alambre)

        alert("Informe", "{0} \n{1} \n{2} \n{3} \n{4}".format(mensaje_punto_a, mensaje_punto_b, mensaje_punto_c, mensaje_punto_d,mensaje_punto_e))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
