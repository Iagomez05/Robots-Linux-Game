from tkinter import *

window = Tk()
window.minsize(height=500,width=400) #Size


def funcion_print():
    ventana = Tk()
    
    boton = Button(ventana,text="ventana nueva")
    boton.pack()
    
    ventana .mainloop()

boton = Button(window,width=10,height=2,bg="blue", text="hola",command=funcion_print) #Color, size and text

boton.place(x=200, y=250)

window.mainloop()
