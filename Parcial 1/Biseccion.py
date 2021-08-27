import math

def funcion_biseccion(funcion,inicio_intervalo,fin_intervalo,iteraciones, tolerancia):
    if funcion(inicio_intervalo)*funcion(fin_intervalo) >= 0:
        print("No funciona metodo de biseccion")
        return None
    aux1 = inicio_intervalo
    aux2 = fin_intervalo
    iteracionN = 1
    #for n in range(1,iteraciones+1):
    condicion = True
    while condicion:
        iteracionN = iteracionN + 1
        medio = (aux1 + aux2)/2
        if funcion(aux1)* funcion(medio) < 0:
            aux2 = medio
        elif funcion(aux2)*funcion(medio) < 0:
            aux1 = medio
        elif funcion(medio) == 0:
            print("Se encontro la solucion exacta")
            print("Iteracion para biseccion",iteracionN)
            return medio
        else:
            print("No se puede usar biseccion")
            return None
        if iteracionN > iteraciones:
            print("Se alcanzo el maximo de iteraciones")
            return (aux1 + aux2)/2
        
        condicion = abs(funcion(medio)) > tolerancia
    ("Se encontro la solucion")
    return (aux1 + aux2)/2