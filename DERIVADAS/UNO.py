print("Para la funcion cuadratica: ")
a=float(input("Ingrese el coeficiente del termino cuadrático: "))
b=float(input("Ingrese el coeficiente lineal: "))
m=float(input("Ingrese el termino independiente: "))
print("")
print("Para la funcion lineal: ")
c=float(input("Ingrese el coeficiente lineal: "))
d=float(input("Ingrese el termino independiente: "))
print("")
print("Para la funcion seno: ")
f=float(input("Ingrese la amplitud: "))



import math

from matplotlib import pyplot

#Funcion exponencial
def f4(j):
    return math.log(j,2.71)

# Función cuadrática.
def f1(x):
    return a*(x**2) + b*(x)+m

# Función lineal.
def f2(x):
    return c*x + d

# Funcion seno
def sen(x):
    return f*math.sin(x/10)
# Valores del eje X que toma el gráfico.
x = range(-100, 150)
j = range(2, 150)

# Graficar ambas funciones.
pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])
pyplot.plot(x, [sen(i) for i in x])
pyplot.plot(j, [f4(i) for i in j])

pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Limitar los valores de los ejes.
pyplot.xlim(-100, 100)
pyplot.ylim(-100, 100)

# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")

# Mostrarlo.
pyplot.show()

