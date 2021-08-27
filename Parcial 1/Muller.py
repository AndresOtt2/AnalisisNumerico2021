
from numpy  import *

#pntB1 es el inicio del intervalo, pntB2 es el fin del intervalo y pntB3 es la estimacion
def Metodo_Muller(f, pntB1,pntB2,pntB3,tolerancia,iteraciones):
    # Metodo de Muller
    p0 = pntB1
    p1 = pntB2
    p2 = pntB3
    k = 3
    while k<=iteraciones:
        c = f(p2)
        b = ((p0-p2)**2 *(f(p1)-f(p2))-(p1-p2)**2 *(f(p0)-f(p2)))/((p0-p2)*(p1-p2)*(p0-p1))
        a = ((p1-p1)*(f(p0)-f(p2)) - (p0-p2)*(f(p1)-f(p2)))/((p0-p2)*(p1-p2)*(p0-p1))
        p3 = p2 - 2*c/(b+(b/abs(b))*sqrt(b**2 -4*a*c))
        #COndicion para la tolerancia
        if abs(p3-p2)<tolerancia:
          print ("Iteracion para Muller",k)
          return p3
        p0 = p1
        p1 = p2
        p2 = p3
        k = k+1
    print ("Se terminaron todas las iteraciones, pero no se alcanzo a cumplir la tolerancia.")
