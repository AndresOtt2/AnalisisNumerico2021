import math
from Biseccion import * 
from Muller import *
from PuntoFijo import *
from Sumatoria import * 
import matplotlib.pyplot as plt

#Ejecucion
#valor tolerancia
#valor tolerancia punto 1
TOL= 10**(-16)
#valor tolerancia punto 2
TOL2= 10**(-5)
#Numero de iteraciones
n=100
#punto de referencia
r=-1
#Inicio intervalo 
inicio = -2
#fin intervalo 
fin=0
#Funciones
f = lambda x: x**3 +2*x+k
g = lambda x: 3*x + math.exp(x) - x**2 + 2
k=math.sqrt(7)
#Funcion g(x) = x para punto fijo
gpuntofijo = lambda x: (-2-math.exp(x))/(3 - x)
#PUNTO 1A
print("PUNTO 1A")
print("Si se toma k como 0, la funcion es equivalente a x**3 + 2x, esta funcion solo tiene tiene como resultado 0 para un valor de x =0 ya que es una funcion de multiplos de x. Esto significa que al añadir el k la funcion se desplaza hacia la izquierda k distancia. Por lo que la raiz se mueve de la misma manera. La raiz entonces siempre sera K y sera unica para cualquier valor que esta pueda tomar\n")
res = funcion_biseccion(f,inicio,fin,n,TOL)
try:
  print('El valor del metodo de biseccion es = %0.8f y  la funcion en este punto = %0.30f' % (res, f(res)))
except OverflowError:
    None
except TypeError:
    None

res = Metodo_Muller(f,-100,100,-3,TOL,n)
try:
  print('El valor del metodo de Muller es = %0.8f y  la funcion en este punto = %0.20f' % (res, f(res)))
except OverflowError:
    None
except TypeError:
    None
#PUNTO 3D
print("\nPUNTO 3D")
res= PuntoFijoCalcular(g,gpuntofijo,r,TOL,n)
try:
  print('El valor del metodo de punto fijo es = %0.8f y  la funcion en este punto = %0.8f' % (res, g(res)))
except OverflowError:
    None
except TypeError:
    None
res = funcion_biseccion(g,inicio,fin,n,TOL)
try:
  print('El valor del metodo de biseccion es = %0.8f y  la funcion en este punto = %0.30f' % (res, g(res)))
except OverflowError:
    None
except TypeError:
    None
#PUNTO 6
print("\nPUNTO 6")
X=Punto6(1.0001,100)
Y=GeoSerie(1.0001,100)
print("el resultado de la sumatoria es", X)
print("el resultado de la serie geometrica es", Y)
print("el error de la multiplicacion anidada es",X-Y)
plt.plot(X)
plt.plot(y)