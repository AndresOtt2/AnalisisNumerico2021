# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 00:35:52 2021

@author: nitro5
"""
import numpy as np
import sympy as sp
import scipy.interpolate as sc
import matplotlib.pyplot as plt
x = np.array([0, 3, 5, 8, 13])
y = np.array([0,225, 383, 623, 993])
z= np.array([75, 77, 80, 74, 72])

#LAGRANGE
poly = sc.lagrange(x, y)
poly2 = sc.lagrange(x, z)
poly3 = np.polyint(poly2)
#RANGO X
a = np.linspace(0, 13, 300) 

b = poly(a)
c = poly2(a)
e = poly3(a)

plt.plot(a, b)
plt.title("Lagrange")
plt.xlabel("tiempo")
plt.ylabel(" distancia")
plt.show()


plt.plot(a, c)
plt.title("LagrangeVT")
plt.xlabel("tiempo")
plt.ylabel("velocidad")
plt.show()


plt.plot(a, e)
plt.title("LagrangeIntegral")
plt.xlabel("tiempo")
plt.ylabel("distancia")
plt.show()


dpoly = poly.deriv()
d= dpoly(a)
plt.plot(a, d)
plt.title("LagrangeDerivada")
plt.xlabel("tiempo")
plt.ylabel("velocidad")
plt.show()


#HERMITE
PolySplineC= sc.CubicSpline(x, y)
h = PolySplineC(a)
plt.plot(a, h)
plt.title("CubicSpline DT")
plt.xlabel("tiempo")
plt.ylabel("distancia")
plt.show()


DSpoly = PolySplineC.derivative()
h2 = DSpoly(a)
plt.plot(a, h2)
plt.title("CubicSpline Derivada")
plt.xlabel("tiempo")
plt.ylabel("velocidad")
plt.show()

PolySplineC2= sc.CubicSpline(x, z)
h = PolySplineC2(a)
plt.plot(a, h)
plt.title("CubicSpline VT")
plt.xlabel("tiempo")
plt.ylabel("Velocidad")
plt.show()

plt.plot(a,c)
plt.plot(a, d)
plt.title("Lagrange VT vs Derivada")
plt.xlabel("tiempo")
plt.ylabel("Velocidad")
plt.show()

plt.plot(a,b)
plt.plot(a, e)
plt.title("Lagrange DT vs IntegraL")
plt.xlabel("tiempo")
plt.ylabel("Velocidad")
plt.show()

maximoDeerivada = np.amax(d)
print("la maxima velocidad para la derivada de lagrange es:", maximoDeerivada)
maximoDeerivada2 = np.amax(c)
print("la maxima velocidad para la interpolacion de lagrange es:", maximoDeerivada2)

dpoly2 = poly2.deriv()
ddpoly = dpoly.deriv()
m= dpoly2(a)
n = ddpoly(a)
plt.plot(a, m)
plt.plot(a,n)
plt.title("Lagrange Derivada VT vs Segunda derivada de Lagrange DT")
plt.xlabel("tiempo")
plt.ylabel("Aceleracion")
plt.show()
    
