import random as rd

muro = "■"
espacio = " "
agente = "×"
espacioRecorrido = "·"


def generar_Mapa(cc, ff):
    laberinto1 = []
    for i in range(0, ff):
        fila_laberinto = []
        for j in range(0, cc):
            fila_laberinto.append(muro)
        laberinto1.append(fila_laberinto)
    i_actual = rd.randrange(ff)
    j_actual = rd.randrange(cc)
    laberinto1[i_actual][j_actual] = espacio
    n_EG = 1
    while n_EG < n_Espacio:
        direccion = rd.randrange(4)
        if direccion == 0 and i_actual > 0:
            i_actual -= 1
        elif direccion == 1 and i_actual < ff - 1:
            i_actual += 1
        elif direccion == 2 and j_actual > 0:
            j_actual -= 1
        else:
            if j_actual < cc - 1:
                j_actual += 1
        if laberinto1[i_actual][j_actual] == muro:
            laberinto1[i_actual][j_actual] = espacio
            n_EG += 1
    return laberinto1


def imprimir(l_i):
    for line in l_i:
        print(" ".join(map(str, line)))


def contar_m(matriz):
    contador = [
        0,
        0,
        0,
        0,
    ]  # contador1:muro; contador2:espacio; contador3:agente; contador4:espaciorecorrido
    for i in range(0, f):
        for j in range(0, c):
            if matriz[i][j] == muro:
                contador[0] += 1
            elif matriz[i][j] == espacio:
                contador[1] += 1
            elif matriz[i][j] == agente:
                contador[2] += 1
            elif matriz[i][j] == espacioRecorrido:
                contador[3] += 1
    return contador


def Agente(lab_ag, ff, cc, np):
    n = 1
    i = rd.randrange(f)
    j = rd.randrange(c)
    while lab_ag[i][j] != espacio:
        i = rd.randrange(f)
        j = rd.randrange(c)
    lab_ag[i][j] = agente
    n_E = (ff * cc) - np
    i_anterior = i
    j_anterior = j
    print("\n Intento " + str(n))
    imprimir(lab_ag)
    while n < n_E:
        direccion = rd.randrange(4)
        if direccion == 0 and i > 0:
            i -= 1
        elif direccion == 1 and i < ff - 1:
            i += 1
        elif direccion == 2 and j > 0:
            j -= 1
        else:
            if j < cc - 1:
                j += 1
        if (
            lab_ag[i][j] != espacioRecorrido
            and lab_ag[i][j] != muro
            and lab_ag[i][j] != agente
        ):
            lab_ag[i_anterior][j_anterior] = espacioRecorrido
            i_anterior = i
            j_anterior = j
            lab_ag[i][j] = agente
            n += 1
            print("\n Intento " + str(n))
            imprimir(lab_ag)


print("LABERINTO\n Laboratorio 1 de SIS420")
c = int(input("Introduzca la cantidad de columnas del laberinto: "))
f = int(input("Introduzca la cantidad de filas del laberinto: "))
n_Pared = int(input("Introduzca la cantidad de muros del laberinto: "))
n_Espacio = (c * f) - n_Pared

laberinto_m = generar_Mapa(c, f)
imprimir(laberinto_m)
Agente(laberinto_m, f, c, n_Pared)
contador = contar_m(laberinto_m)
print("Hay " + str(contador[0]) + " muros.")
print("Hay " + str(contador[1]) + " espacio.")
print("Hay " + str(contador[2]) + " agente.")
print("Hay " + str(contador[3]) + " espacio recorrido.")
