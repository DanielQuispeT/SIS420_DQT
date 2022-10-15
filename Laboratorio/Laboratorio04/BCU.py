## Integrangte: Quispe Taboada Daniel 
# #


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
        nodos_frontera = sorted(nodos_frontera, key=Comparar)
        nodo_actual = nodos_frontera.pop(0)
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            
            lista_hijos = nodos_hijos(nodo_actual)
            for hijo in lista_hijos:
                
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    
                    for n in nodos_frontera:
                        print("entro")
                        if n.get_costo() > hijo.get_costo():
                            nodo_actual.set_hijo(hijo)
                            nodos_frontera.append(hijo)
                            nodos_frontera.remove(n)
                            


def nodos_hijos(nodo):
    hijos = []
    n = len(nodo.get_datos())
    i = 0
    while i < n-1:
        hijo_datos = nodo.get_datos().copy()
        temp = hijo_datos[i]
        hijo_datos[i] = hijo_datos[i+1]
        hijo_datos[i+1] = temp
        hijo = Nodo(hijo_datos)
        nodo.set_hijo(hijo)
        hijos.append(hijo)
        i += 1
    return hijos


if __name__ == "__main__":
    estado_inicial = [5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5]
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
