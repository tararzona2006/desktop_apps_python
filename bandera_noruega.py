from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera de Noruega")

ventana_principal.geometry("1000x500")

ventana_principal.config(bg="gray6")

#---------------------------------
# frame rojo
#---------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="red" , width=1000, height=1000)
frame_amarillo.place(x=0, y=0)

#---------------------------------
# frame blanco
#---------------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="white" , width=100, height=1000)
frame_blanco.place(x=300, y=0)

#---------------------------------
# frame Blanco
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="white" , width=1000, height=100)
frame_azul.place(x=0, y=200)

#---------------------------------
# frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue" , width=50, height=1000)
frame_azul.place(x=325, y=0)

#---------------------------------
# frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue" , width=1000, height=50)
frame_azul.place(x=0, y=225)



ventana_principal.mainloop()