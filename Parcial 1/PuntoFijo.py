import math
def PuntoFijoCalcular(funcion,funcion2, referencia, tolerancia, iter):
    iteracionN = 1
    aux = 1
    condicion = True
    while condicion:
        x = funcion2(referencia)
        #print('Iteracion numero %d, el valor del punto fijo = %0.6f y  la funcion en este punto = %0.6f' % (iteracionN, x, funcion(x)))
        referencia = x

        iteracionN = iteracionN + 1
        
        if iteracionN > iter:
            aux=0
            print("Se alcanzo el maximo de iteraciones")
            break
        
        condicion = abs(funcion(x)) > tolerancia
        
    if aux==1:
        print ("Se encontro la solución exacta")
        print ("Iteracion para Punto Fijo", iteracionN)
        
    else:
      print ("Iteracion para Punto Fijo", iteracionN)
    return x;