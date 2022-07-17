# import la libreria tkinter, con el alias tk
import tkinter as tk
import random


def mensaje_piedra():
    eleccion_cpu = random.randint(0, 2)
    label_respuesta.config(text=eleccion_cpu)

    if eleccion_cpu == 0:
        label_resultado.config(text="Empate")

    elif eleccion_cpu == 1:
        label_resultado.config(text="Derrota")

    elif eleccion_cpu == 2:
        label_resultado.config(text="Victoria")


def mensaje_papel():
    eleccion_cpu = random.randint(0, 2)

    if eleccion_cpu == 0:
        label_resultado.configure(text="Victoria")

    elif eleccion_cpu == 1:
        label_resultado.configure(text="Empate")

    elif eleccion_cpu == 2:
        label_resultado.configure(text="Derrota")


def mensaje_tijera():
    eleccion_cpu = random.randint(0, 2)

    if eleccion_cpu == 0:
        label_resultado.configure(text="Derrota")

    elif eleccion_cpu == 1:
        label_resultado.configure(text="Victoria")

    elif eleccion_cpu == 2:
        label_resultado.configure(text="Empate")


def reinicio():
    ventana_principal.destroy()


# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------

# Creación objeto Tk (ventana principal)
ventana_principal = tk.Tk()

# titulo ventana principal
ventana_principal.title("PIEDRA PAPEL O TIJERA")

# dimensaiones d ela ventana
ventana_principal.geometry("900x600")

# desabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo a la ventana principal
ventana_principal.config(bg="gray")

# icono de la ventana
# ventana_principal.iconbitmap("papel.ico.ico")

# -------------------------------
# FRAME ENTRADA DE DATOS
# -------------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(background="#FFAC33", width="880", height="580")
frame_entrada.place(x=10, y=10)

# etiqueta para el titulo
titulo = tk.Label(frame_entrada, text="PIEDRA PAPEL O TIJERA")
titulo.config(bg="#FFAC33", fg="black", font=("Arial, 14"))
titulo.place(x=350, y=10)

# imagen piedra
logo_piedra = tk.PhotoImage(file="piedra.png")
label_piedra = tk.Label(frame_entrada, image=logo_piedra)
label_piedra.place(x=10, y=100)

# imagen papel
logo_papel = tk.PhotoImage(file="papel.png")
label_papel = tk.Label(frame_entrada, image=logo_papel)
label_papel.place(x=330, y=100)

# imagen tijera
logo_tijera = tk.PhotoImage(file="tijera.png")
label_tijera = tk.Label(frame_entrada, image=logo_tijera)
label_tijera.place(x=640, y=100)

# etiqueta x
label_x = tk.Label(frame_entrada, text="JAIRO ARMANDO CARDOZO MENDOZA")
label_x.config(bg="black", fg="white", font=("Arial, 14"))
label_x.place(x=300, y=50)

# etiqueta resultado
label_resultado = tk.Label(frame_entrada, text="")
label_resultado.config(bg="#FFAC33", fg="black", font=("Arial, 14"))
label_resultado.place(x=420, y=490)

label_respuesta = tk.Label(frame_entrada, text="")
label_respuesta.place(x=300, y=400)
# -------------------------------
# FRAME OPERACIONES
# -------------------------------

# boton piedra
boton_piedra = tk.Button(frame_entrada, text="PIEDRA", command=mensaje_piedra)
boton_piedra.place(x=120, y=400)

# boton papel
boton_papel = tk.Button(frame_entrada, text="PAPEL", command=mensaje_papel)
boton_papel.place(x=430, y=400)

# boton tijera
boton_tijera = tk.Button(frame_entrada, text="TIJERA", command=mensaje_tijera)
boton_tijera.place(x=740, y=400)

# boton reinicio
boton_reinicio = tk.Button(frame_entrada, text="REINICIO", command=reinicio)
boton_reinicio.place(x=420, y=450)

# -------------------------------
# FRAME RESULTADOS
# -------------------------------

# desplegar ventana principal y queda a la espera de lo que el usuario haga
ventana_principal.mainloop()
