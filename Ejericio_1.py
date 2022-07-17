from tkinter import Tk, Label

#Crea una ventana llamada root, de la clase Tk. Se crea un objeto de la clase Tk
root = Tk()

#Definimos el tamaño de la ventana 
root.geometry("500x500")

root.resizable(True, False)

root.minsize(50,50)
root.maxsize(500, 500)

#Agregamos etiqueta de ventana 
etiqueta = Label(text="BIENVENIDOS A LA \nUNIVERSIDAD INDUSTRIAL DE SANTANDER \nSEDE EL SOCORRO\n")
etiqueta.pack()

#Muestra la ventana y entra en un blucle infinito para la antencion de los evento.
root.mainloop()