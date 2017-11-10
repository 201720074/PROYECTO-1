import tkinter as tk
ven=tk.Tk()
ven.title("graficador")
ven.geometry("300x300")
ven.configure(bg="black")

e1=tk.Label(text="Que funcion quiere?",bg="black",fg="white")
e1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
ent=tk.Entry()
ent.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
ven.mainloop()

