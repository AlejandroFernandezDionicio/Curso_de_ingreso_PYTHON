import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre:Alejandro Melnic
Apellido:Fernandez Dionicio
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el 
botón ‘Informar’ indicar el punto cardinal de nuestro país donde se encuentra: 
Norte, Sur, Este u Oeste
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        Destino = self.combobox_destino.get()

        match Destino:
            case "Bariloche":
                Mensaje = "Se encuentra en el oeste"
            case "Mar del plata":
                Mensaje = "Se encuentra en el este"
            case "Cataratas":
                Mensaje = "Se encuentra en el norte"
            case "Ushuaia":
                Mensaje = "Se encuentra en el sur"

        alert(title = "EJ 07", message= Mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()