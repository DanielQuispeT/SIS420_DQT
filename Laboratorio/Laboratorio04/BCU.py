## Integrangte: Quispe Taboada Daniel 
#   Se pudo resolver agregando un costo a cada nodo aleatoriamente que 
#   ronda entre los 10 y 100 de nodo a nodo, con ello se va viendo lo que 
#   costaria llegar de un estado a otro, se puede realizando el de menor 
#   costo y el de mayor costo con la modificación de la lista de nodos 
#   frontera se puede resolver con facilidad hasta los 6 datos, despues 
#   con mas datos puede tardar demasiado#


import random as rd
import time
from nodo import *
def Comparar(nodo):
    return nodo.get_costo()

def Busqueda(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodo_inicio.set_costo(0)
    nodos_frontera.append(nodo_inicio)
    
    while resuelto == False and len(nodos_frontera) != 0:
        nodos_frontera = sorted(nodos_frontera, key=Comparar, reverse=True) #reverse=True me ordena de mayor a menor y reverse=False ordena menor a mayor 
        '''for i in nodos_frontera:
            print('Datos: ',i.get_datos(),' Costo: ',i.get_costo())
        print('-------------------------')'''
        nodo_actual = nodos_frontera[0]
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            lista_hijos = nodos_hijos(nodo_actual)
            for hijo in lista_hijos:
                if not hijo.en_lista(nodos_visitados):
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:

                            if n.equal(hijo) and n.get_costo() > hijo.get_costo():
                                nodo_actual.set_hijo(hijo)
                                nodos_frontera.append(hijo)
                                nodos_frontera.remove(n)
                    else:
                        nodos_frontera.append(hijo)
                            


def nodos_hijos(nodo):
    hijos = []
    n = len(nodo.get_datos())
    i = 0
    costo = nodo.get_costo()
    while i < n-1:
        hijo_datos = nodo.get_datos().copy()
        temp = hijo_datos[i]
        hijo_datos[i] = hijo_datos[i+1]
        hijo_datos[i+1] = temp
        hijo = Nodo(hijo_datos)
        costo_h = rd.randrange(10, 100)
        hijo.set_costo(costo_h + costo)
        nodo.set_hijo(hijo)
        hijos.append(hijo)
        i += 1
    return hijos

def generar_Lista(n):
    lista = []
    for i in range(n):
        lista.append(i+1)
    return lista

if __name__ == "__main__":
    n = int(input('Tamaño de la lista: '))
    lista = generar_Lista(n)
    estado_inicial = list(reversed(lista))
    solucion = list(lista)
    inicio = time.time()
    nodo_solucion = Busqueda(estado_inicial, solucion)
    fin = time.time()
    print('Tiempo de ejecucion: ', fin - inicio, 'seg.')
    
    resultado = []
    resultado_costo = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        resultado_costo.append(nodo_actual.get_costo())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado_costo.append(0)
    resultado.reverse()
    resultado_costo.reverse()

    print('\nMovimientos:')
    for i in range(len(resultado)):
        print(i,resultado[i], ' Costo: ', resultado_costo[i])
    print("Costo: %s" % str(nodo_solucion.get_costo()))
