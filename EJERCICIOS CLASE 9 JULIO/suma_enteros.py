#import la libreria tkinter, con el alias tk
from pydoc import plain
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# FUNCIONES OPERACIONES
# -------------------------------
def calcular():
    messagebox.showinfo("Suma enteros", "La suma es...")
    r = x.get() + y.get()
    at_resultados.insert(tk.INSERT, str(x.get()) + "+" + str(y.get()) + "=" + str(r)+"\n")

def borrar():
    messagebox.showinfo("Suma enteros", "Los datos seran borrados.....")
    x.set(0)
    y.set(0)
    at_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("suma_enteros", "hizo clik en el boton salir")
    ventana_principal.destroy()

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
ventana_principal.config(bg="gray")

# icono de la ventana
ventana_principal.iconbitmap("sum_ico.ico")

# -------------------------------
# VARIABLES DE CONTROL
# -------------------------------
x=tk.IntVar()
y=tk.IntVar()
z=tk.IntVar()

# -------------------------------
# FRAME ENTRADA DE DATOS
# -------------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(background="#64b446" , width="480", height="240")
frame_entrada.place(x=10, y=10)

#etiqueta para el titulo
titulo = tk.Label(frame_entrada, text="SUMA DE ENTEROS")
titulo.config(bg="#64b446", fg="black", font=("Arial, 12"))
titulo.place(x=200, y=10)

# imagen
logo_uis = tk.PhotoImage(file="uis.png")
label_logo = tk.Label(frame_entrada, image=logo_uis)
label_logo.place(x=10, y=40)

#etiqueta x
label_x = tk.Label(frame_entrada , text= "X =")
label_x.config(bg="#64b446", fg="black", font=("Arial, 14"))
label_x.place(x=250, y=50)

#caja de texto para x
entry_x = tk.Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Arial, 12"))
entry_x.focus_set()
entry_x.place(x=290 , y=50)

#etiqueta y
label_y = tk.Label(frame_entrada , text= "Y =")
label_y.config(bg="#64b446", fg="black", font=("Arial, 14"))
label_y.place(x=250, y=100)

#caja de texto para y
entry_y = tk.Entry(frame_entrada, textvariable=y)
entry_y.config(font=("Arial, 12"))
entry_y.place(x=290 , y=100)

# -------------------------------
# FRAME OPERACIONES
# -------------------------------
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg="#64b446" , width="480" ,height="120")
frame_operaciones.place(x=10, y=255)

#boton calcular
boton_calcular = tk.Button(frame_operaciones, text="CALCULAR", command=calcular)
boton_calcular.place(x=10, y=60)

#boton borrar
boton_borrar = tk.Button(frame_operaciones, text="BORRAR", command=borrar)
boton_borrar.place(x=160, y=60)

#boton salir
boton_salir = tk.Button(frame_operaciones, text="SALIR", command=salir)
boton_salir.place(x=320, y=60)

# -------------------------------
# FRAME RESULTADOS
# -------------------------------
frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(bg="#64b446" , width="480", height="110")
frame_resultados.place(x=10, y=380)

# area de texto de resultados
at_resultados = tk.Text(frame_resultados)
at_resultados.config(width=57 , height=5)
at_resultados.place(x=10 , y=10)

# desplegar ventana principal y queda a la espera de lo que el usuario haga 
ventana_principal.mainloop()