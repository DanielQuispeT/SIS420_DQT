## Integrangtes: Quispe Taboada Daniel
# Laboratorio 02_ 
# El programa en mi pc soporta hasta 7 valores en la
# lista, pero con mas de eso se queda demasiado 
# procesando, con 7 valores en la lista el tiempo de 
# ejecucion tarda entre 16 y 18 segundos.
# El problema es que se crea nodos inutiles algunos
# que sus hijos no llevan a ningun lugar y otros que
# la solucion esta muy profundo en el arbol, para 
# solucionar la creacion de nodos innecesarios se podria
# poner un determinado costo a los estados que favorecer 
# encontrar la solucion, o con una busqueda informada.#


import time
from nodo import *


def Busqueda(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)

    while resuelto == False and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            n = len(nodo_actual.get_datos().copy())
            for i in range(n-1):
                hijo_datos = nodo_actual.get_datos().copy()
                temp = hijo_datos[i]
                hijo_datos[i] = hijo_datos[i+1]
                hijo_datos[i+1] = temp
                hijo = Nodo(hijo_datos)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)

def generar_Lista(n):
    lista = []
    for i in range(n):
        lista.append(i+1)
    return lista


if __name__ == "__main__":
    n = 7
    lista = generar_Lista(n)
    estado_inicial = list(reversed(lista))
    solucion = list(lista)
    inicio = time.time()
    nodo_solucion = Busqueda(estado_inicial, solucion)
    fin = time.time()
    print('Tiempo de ejecucion: ', fin - inicio, 'seg.')
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print('\nMovimientos:')
    for i in resultado:
        print(i)
