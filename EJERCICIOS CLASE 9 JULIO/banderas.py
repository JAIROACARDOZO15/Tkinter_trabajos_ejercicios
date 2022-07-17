#import la libreria tkinter, con el alias tk
import tkinter as tk

# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------

#Creación objeto Tk (ventana principal)
ventana_principal = tk.Tk()

#titulo ventana principal
ventana_principal.title("Suma enteros")

# dimensaiones d ela ventana
ventana_principal.geometry("500x500")

#desabilitar boton maximizar 
ventana_principal.resizable(0,0)

#color de fondo a la ventana principal
ventana_principal.config(bg="red")

# icono de la ventana
ventana_principal.iconbitmap("sum_ico.ico")

# -------------------------------
# FRAME ENTRADA DE DATOS
# -------------------------------

frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(background="white" , width="100", height="300")
frame_entrada.place(x=200 , y=100)

# -------------------------------
# FRAME OPERACIONES
# -------------------------------
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(background="white" , width="300" ,height="100")
frame_operaciones.place(x=100 , y=200)


# desplegar ventana principal y queda a la espera de lo que el usuario haga 
ventana_principal.mainloop()