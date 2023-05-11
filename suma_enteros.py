from tkinter import *

# se importa la libreria tkintercon todas sus funciones
from tkinter import *
from tkinter import messagebox
#-----------------------
# funciones de la app
#-----------------------
# sumar
def sumar():
    pass

# borrar
def borrar():
    pass

# salir 
def salir():
    messagebox.showinfo("mini calcuadora 1.0","la app se va serrar")
    ventana_principal.destroy()
#-----------------------------
# ventana principal de la app
#-----------------------------

ventana_principal= Tk()

ventana_principal.title("mini calculadora 1.0")

ventana_principal.geometry("500x500")

ventana_principal.resizable(False,False)

# color de la ventana
ventana_principal.config(bg=("red"))

# frame de entrada de datosf
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo=PhotoImage(file="escudo_colegio.png")
lb_logo=Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo=Label(frame_entrada, text="suma enteros 1.0")
titulo.config(bg="red", fg="white", font=("Arial",16))
titulo.place(x=240,y=10)

# etiqueta para valor de x
lb_x = Label(frame_entrada, text = "x = ")
lb_x.config(bg="white", fg="red", font=("helvetica", 18))
lb_x.place(x=240, y=60)

# caja de texto para valor x
entry_x = Entry(frame_entrada)
entry_x.config (bg="white", fg="red", font=("tienes new roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=290, y=60)

# etiqueta para valor de y
lb_y = Label(frame_entrada, text = "y = ")
lb_y.config(bg="white", fg="red", font=("helvetica", 18))
lb_y.place(x=240, y=120)
# caja de texto para valor de y
entry_y = Entry(frame_entrada)
entry_y.config (bg="white", fg="red", font=("tienes new roman", 18), width=6)
entry_y.focus_set()
entry_y.place(x=290, y=120)

# frame de operacion
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)


# boton para sumar
bt_sumar = Button(frame_operaciones, text="sumar",command=sumar)
bt_sumar.place(x=45,y=35,width=100, height=30)

# boton para borrar 
bt_borrar = Button(frame_operaciones, text="borrar",command=borrar)
bt_borrar.place(x=190,y=35,width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones, text="salir", command=salir)
bt_salir.place(x=335,y=35,width=100, height=30)

# frame del resultado
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="white", width=480, height=180)
frame_resultado.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(frame_resultado)
t_resultados.config(bg="black",fg="green yellow", font=("courrier", 20))
t_resultados.place(x=10,y=10, width=460, height=160)

ventana_principal.mainloop()