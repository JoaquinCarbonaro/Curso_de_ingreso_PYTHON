import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
apellido: del Rio
Nombre: Tomas

Enunciado:
Elecciones Presidenciales:
Se pide un programa que agrega las edades de los votantes en distintas listas dependiendo de la persona votada.
Ademas se realizaran informes sobre los datos cargados.

* Edad: Por Textbox 
* Nacionalidad: Por ComboBox ("Argentino", "Extranjero", "Naturalizado")
* Voto: Por prompt ("Massa", "Milei", "Larreta")

-La Edad minima de voto es 16 años para los Argentinos, 18 años para los Naturalizados y los Extranjeros no pueden votar.
-La Edad ingresada no debe superar los 115 años

A)  Al presionar el botón 'Votar' si la edad es valida y la persona no es extranjera se debera preguntar a quien va dirigido el voto y cargarlo
en la lista correspondiente.

Si La persona no puede votar indicarlo por un Alert
Si la persona puede votar validar que el votante sea valido
Si se voto correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar los votos de cada participante con el siguiente formato:
(i = Indice)
Votantes de Massa:
i Edad
0 17
1 42
2 32
Votantes de Milei:
i Edad
0 25
1 22
2 32
Votantes de Larreta:
i Edad
0 16
1 23
2 45

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar 
    0- Informar Del mayor votante de Milei o Massa posicion y edad.
    1- Informar Del menor votante de Larreta o Milei posicion y edad.
    2- Informar Promedio de Edades De los votantes de Milei y Larreta
    3- Informar Promedio de Edades De los votantes de Massa y Larreta
    4- Informar las edades que superan el promedio total
    5- Informar las edades que NO superan el promedio total de edad
    6- Informar Porcentaje de votos de cada participante
    7- Informar la cantidad de votantes que NO superan el promedio total de edades
    8- Informar el ganador de las elecciones (Suponiendo que solo hay uno, El que mas votos tuvo).
    9- Indicar que candidato tiene el mayor promedio de edad entre sus votantes
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")

        self.txt_edad = customtkinter.CTkEntry(master=self, placeholder_text="Edad")
        self.txt_edad.grid(row=1, padx=20, pady=20)

        self.combobox_nacionalidad = customtkinter.CTkComboBox(master=self, values=["Argentino", "Extranjero", "Naturalizado"])
        self.combobox_nacionalidad.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_votar = customtkinter.CTkButton(master=self, text="Votar", command=self.btn_votar_on_click)
        self.btn_votar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar_1= customtkinter.CTkButton(master=self, text="Informar 1", command=self.btn_informar_1_onclick)
        self.btn_informar_1.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")     

        self.btn_informar_2= customtkinter.CTkButton(master=self, text="Informar 2", command=self.btn_informar_2_onclick)
        self.btn_informar_2.grid(row=6, padx=20, pady=20, columnspan=2, sticky="nsew")    

        self.lista_edades_massa = [62, 73, 63]
        self.lista_edades_milei = [61, 77, 68]
        self.lista_edades_larreta = [67, 74, 61]

    def btn_votar_on_click(self):
        # -La Edad minima de voto es 16 años para los Argentinos, 18 años para los Naturalizados y los Extranjeros no pueden votar. x
        # -La Edad ingresada no debe superar los 115 años 
        #A)  Al presionar el botón 'Votar' si la edad es valida y la persona no es extranjera se debera preguntar a quien va dirigido el voto y cargarlo en la lista correspondiente.
        # Si La persona no puede votar indicarlo por un Alert
        # Si la persona puede votar validar que el votante sea valido
        # Si se voto correctamente indicarlo con un Alert
        # -- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --\

        edad = self.txt_edad.get()
        nacionalidad = self.combobox_nacionalidad.get()

        if edad.isdigit():
            edad = int(edad)
            if (edad >= 16 and edad <= 115 and nacionalidad == 'Argentino') or (edad >= 18 and edad <= 115 and nacionalidad == 'Naturalizado'):
                voto_dirigido = prompt('Elecciones', 'Elija el candidadto que quiere votar "Massa", "Milei", "Larreta"')
                while voto_dirigido == '' or voto_dirigido == None or (voto_dirigido != 'Massa' and voto_dirigido != 'Milei' and voto_dirigido != 'Larreta' ):
                    voto_dirigido = prompt('Elecciones', 'Elija el candidadto que quiere votar "Massa", "Milei", "Larreta"')
                if voto_dirigido == 'Massa':
                    self.lista_edades_massa.append(edad)
                    alert('Elecciones', 'Voto cargado correctamente')
                elif voto_dirigido == 'Milei':
                    self.lista_edades_milei.append(edad)
                    alert('Elecciones', 'Voto cargado correctamente')
                elif voto_dirigido == 'Larreta':
                    self.lista_edades_larreta.append(edad)
                    alert('Elecciones', 'Voto cargado correctamente')
                else:
                    alert('Elecciones', 'Ingrese un candito valido')
            else:
                alert('Elecciones', 'Pueden votar los argentinos mayores de 16 años y los naturalizados mayores de 18. Los extranjeros no pueden votar. Ademas la edad ingresada no debe superar los 115 años.')
        else:
            alert('Elecciones', 'La edad ingresada debe ser un numero')
        
    def btn_mostrar_on_click(self):

        print('Votantes de Massa:')
        for i in range(len(self.lista_edades_massa)):
            print(f'{i} {self.lista_edades_massa[i]}')

        print('Votantes de Milei:')
        for i in range(len(self.lista_edades_milei)):
            print(f'{i} {self.lista_edades_milei[i]}')

        print('Votantes de Larreta:')
        for i in range(len(self.lista_edades_larreta)):
            print(f'{i} {self.lista_edades_larreta[i]}')

    def btn_informar_1_onclick(self):
        # 4- Informar las edades que superan el promedio total
        acumulador_edades_massa = 0
        contador_edades_massa_superan_promedio = 0

        for i in range(len(self.lista_edades_massa)):
            acumulador_edades_massa += self.lista_edades_massa[i]
        
        promedio_edades_massa = acumulador_edades_massa / len(self.lista_edades_massa)
        
        for edad in self.lista_edades_massa:
            if promedio_edades_massa < edad:
                contador_edades_massa_superan_promedio += 1

        print('El promedio de las edades de los votantes de massa es: {0:.2f} Hay {1} votantes que superan el promedio'.format(promedio_edades_massa, contador_edades_massa_superan_promedio))

        acumulador_edades_milei = 0
        contador_edades_milei_superan_promedio = 0

        for i in range(len(self.lista_edades_milei)):
            acumulador_edades_milei += self.lista_edades_milei[i]
        
        promedio_edades_milei = acumulador_edades_milei / len(self.lista_edades_milei)
        
        for edad in self.lista_edades_milei:
            if promedio_edades_milei < edad:
                contador_edades_milei_superan_promedio += 1

        print('El promedio de las edades de los votantes de milei es: {0:.2f} Hay {1} votantes que superan el promedio'.format(promedio_edades_milei, contador_edades_milei_superan_promedio))

        acumulador_edades_larreta = 0
        contador_edades_larretra_superan_promedio = 0

        for i in range(len(self.lista_edades_larreta)):
            acumulador_edades_larreta += self.lista_edades_larreta[i]
        
        promedio_edades_larreta = acumulador_edades_larreta / len(self.lista_edades_larreta)
        
        for edad in self.lista_edades_larreta:
            if promedio_edades_larreta < edad:
                contador_edades_larretra_superan_promedio += 1

        print('El promedio de las edades de los votantes de larreta es: {0:.2f} Hay {1} votantes que superan el promedio'.format(promedio_edades_larreta, contador_edades_larretra_superan_promedio))

        contador_edades_total_superan_promedio = 0

        acumulador_edades_total = acumulador_edades_larreta + acumulador_edades_milei + acumulador_edades_massa
        indice_total = len(self.lista_edades_massa) + len(self.lista_edades_milei) + len(self.lista_edades_larreta)
        promedio_edades_total = acumulador_edades_total / indice_total

        for edad in self.lista_edades_larreta:
            if promedio_edades_total < edad:
                contador_edades_total_superan_promedio += 1

        for edad in self.lista_edades_milei:
            if promedio_edades_total < edad:
                contador_edades_total_superan_promedio += 1
        
        for edad in self.lista_edades_massa:
            if promedio_edades_total < edad:
                contador_edades_total_superan_promedio += 1

        print('El promedio de las edades totales de los votantes es: {0:.2f} Hay {1} votantes que superan el promedio'.format(promedio_edades_total, contador_edades_total_superan_promedio))

    def btn_informar_2_onclick(self):
        #5- Informar las edades que NO superan el promedio total de edad
        acumulador_edades_massa = 0
        contador_edades_massa_nosuperan_promedio = 0

        for i in range(len(self.lista_edades_massa)):
            acumulador_edades_massa += self.lista_edades_massa[i]
        
        promedio_edades_massa = acumulador_edades_massa / len(self.lista_edades_massa)
        
        for edad in self.lista_edades_massa:
            if promedio_edades_massa > edad:
                contador_edades_massa_nosuperan_promedio += 1

        print('El promedio de las edades de los votantes de massa es: {0:.2f} Hay {1} votantes que no superan el promedio'.format(promedio_edades_massa, contador_edades_massa_nosuperan_promedio))

        acumulador_edades_milei = 0
        contador_edades_milei_nosuperan_promedio = 0

        for i in range(len(self.lista_edades_milei)):
            acumulador_edades_milei += self.lista_edades_milei[i]
        
        promedio_edades_milei = acumulador_edades_milei / len(self.lista_edades_milei)
        
        for edad in self.lista_edades_milei:
            if promedio_edades_milei >= edad:
                contador_edades_milei_nosuperan_promedio += 1

        print('El promedio de las edades de los votantes de milei es: {0:.2f} Hay {1} votantes que no superan el promedio'.format(promedio_edades_milei, contador_edades_milei_nosuperan_promedio))

        acumulador_edades_larreta = 0
        contador_edades_larretra_nosuperan_promedio = 0

        for i in range(len(self.lista_edades_larreta)):
            acumulador_edades_larreta += self.lista_edades_larreta[i]
        
        promedio_edades_larreta = acumulador_edades_larreta / len(self.lista_edades_larreta)
        
        for edad in self.lista_edades_larreta:
            if promedio_edades_larreta >= edad:
                contador_edades_larretra_nosuperan_promedio += 1

        print('El promedio de las edades de los votantes de larreta es: {0:.2f} Hay {1} votantes que no superan el promedio'.format(promedio_edades_larreta, contador_edades_larretra_nosuperan_promedio))

        contador_edades_total_nosuperan_promedio = 0

        acumulador_edades_total = acumulador_edades_larreta + acumulador_edades_milei + acumulador_edades_massa
        indice_total = len(self.lista_edades_massa) + len(self.lista_edades_milei) + len(self.lista_edades_larreta)
        promedio_edades_total = acumulador_edades_total / indice_total

        for edad in self.lista_edades_larreta:
            if promedio_edades_total >= edad:
                contador_edades_total_nosuperan_promedio += 1

        for edad in self.lista_edades_milei:
            if promedio_edades_total >= edad:
                contador_edades_total_nosuperan_promedio += 1
        
        for edad in self.lista_edades_massa:
            if promedio_edades_total >= edad:
                contador_edades_total_nosuperan_promedio += 1

        print('El promedio de las edades totales de los votantes es: {0:.2f} Hay {1} votantes que no superan el promedio'.format(promedio_edades_total, contador_edades_total_nosuperan_promedio))

if __name__ == "__main__":
    app = App()
    app.geometry("300x400")
    app.mainloop()
