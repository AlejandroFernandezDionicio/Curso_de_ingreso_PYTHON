import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
NOMBRE:Alejandro Melnic
APELLIDO:Fernandez Dionicio

Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “"FelipeLamparas"” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()

        cantidad_lamparitas = self.combobox_cantidad.get()
        cantidad_lamparitas = int(cantidad_lamparitas)

        precio = 800

        precio_lamparitas = precio * cantidad_lamparitas


        if cantidad_lamparitas >= 6 :
            Descuento = 50  
            
        elif cantidad_lamparitas == 5 :
            if marca == "ArgentinaLuz" :
                Descuento = 40
            else:
                Descuento = 30

        elif cantidad_lamparitas == 4 :
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas" :
                Descuento = 25
            else:
                Descuento = 20

        elif cantidad_lamparitas == 3 :
            if marca == "ArgentinaLuz":
                Descuento = 15
            elif marca == "FelipeLamparas":
                Descuento = 10
            else:
                Descuento = 5

        else:
            Descuento = 0

        precio_final = precio_lamparitas * Descuento / 100

        Precio_descuento = precio_lamparitas - precio_final   
        
        mensaje = "EL precio final es de {0}".format(Precio_descuento)

        if Precio_descuento >= 4000 :
            Descuento_Adicional = Precio_descuento * 5 / 100
            Resultado_Final_Descuento = Precio_descuento - Descuento_Adicional
            mensaje = "El precio final es de {0}".format(Resultado_Final_Descuento)

        alert(title = "TP", message = mensaje)




        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()