import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre:Alejandro Melnic
Apellido:Fernandez Dionicio
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        estaciones = self.combobox_estaciones.get()
        destinos = self.combobox_destino.get()

        aumento_20 = 15000 + 15000 * 20 / 100
        aumento_10 = 15000 + 15000 * 10 / 100

        descuento_20 = 15000 - 15000 * 20 / 100
        descuento_10 = 15000 - 15000 * 10 / 100

        match estaciones:
            case "Invierno":
                match destinos:
                    case "Bariloche":
                        mensaje = "La tarifa total es de {0}".format(aumento_20)
                    case "Cataratas" | "Cordoba":
                        mensaje = "La tarifa total es de {0}".format(descuento_10)
                    case "Mar del plata":
                        mensaje = "La tarifa total es de {0}".format(descuento_20)
            case "Verano":
                match destinos:
                    case "Bariloche":
                        mensaje = "La tarifa total es de {0}".format(descuento_20)
                    case "Cataratas" | "Cordoba":
                        mensaje = "La tarifa total es de {0}".format(aumento_10)
                    case "Mar del plata":
                        mensaje = "La tarifa total es de {0}".format(aumento_20)
            case "Primavera" | "Otoño":
                match destinos:
                    case "Barioche" | "Cataratas" | "Mar del plata":
                        mensaje = "La tarifa total es de {0}".format(aumento_10)
                    case "Cordoba":
                        mensaje = "La tarifa total es de 15000"

        alert(title = "EJ 09", message = mensaje)




    


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()