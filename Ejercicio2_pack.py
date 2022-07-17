from tkinter import Tk, Label, TOP, BOTTOM , RIGHT , LEFT

#Crea una ventana llamada root, de la clase Tk. Se crea un objeto de la clase Tk
root = Tk()

#Definimos el tamaño de la ventana 
root.geometry("500x500")

root.resizable(True, False)

root.minsize(50,50)
root.maxsize(500, 500)

#Agregamos etiqueta de ventana 
etiqueta1 = Label(text="UIS SOCORRO 1")
etiqueta2 = Label(text="UIS SOCORRO 2")
etiqueta3 = Label(text="UIS SOCORRO 3")
etiqueta4 = Label(text="UIS SOCORRO 4")

etiqueta1.pack(side = TOP, padx=10,pady=20)
etiqueta2.pack(side = BOTTOM,padx=10,pady=20)
etiqueta3.pack(side = LEFT,padx=10,pady=20)
etiqueta4.pack(side = RIGHT,padx=10,pady=20)

#Muestra la ventana y entra en un blucle infinito para la antencion de los evento.
root.mainloop()