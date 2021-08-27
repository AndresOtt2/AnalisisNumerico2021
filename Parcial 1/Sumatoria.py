from numpy import *
def Punto6(x, n):
  total=0
  coeficientes= ones(n)
  for i in range(n):
    if i%2!=0:
      coeficientes[i]=coeficientes[i]*-1
    total=total+(coeficientes[i]*(x**i))
  return total

def GeoSerie(x,n):
  r=((1-x**n)/(1+x))
  return r

  
    
  