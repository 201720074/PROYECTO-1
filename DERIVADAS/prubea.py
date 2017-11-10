from tkinter import *
ventana=Tk()
ventana.geometry("500x300+100+100")
ventana.title("campo de texto")
usuario=Label(text="Ingrese la los coeficientes",font=("Agency FB",14)).place(x=0,y=10)
entrada=StringVar()
entrada.set("ingrese dato")
cajita=Entry(ventana,textvariable=entrada).place(x=50,y=100)
ventana.mainloop()