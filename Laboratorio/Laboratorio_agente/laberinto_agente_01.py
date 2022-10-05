import random as rd

muro = "#"
espacio = " "
agente = "*"
espacioRecorrido = "·"
pelota = 'o'


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
    n_p = 0
    while n_p < n_Pelota:
        ii = rd.randrange(ff)
        jj = rd.randrange(cc)
        if laberinto1[ii][jj] == espacio:
            laberinto1[ii][jj] = pelota
            n_p += 1
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
        0
    ]  # contador0:muro; contador1:espacio; contador2:agente; contador3:espaciorecorrido; contador4: pelota
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
            elif matriz[i][j] == pelota:
                contador[4] += 1
    return contador


def Agente(lab_ag, ff, cc, n_P):
    n = 0
    intento = 1
    i = rd.randrange(f)
    j = rd.randrange(c)
    while lab_ag[i][j] != espacio:
        i = rd.randrange(f)
        j = rd.randrange(c)
    lab_ag[i][j] = agente
    i_anterior = i
    j_anterior = j
    print(" Intento " + str(intento))
    print("    i: "+str(i)+"\n    j: "+str(j))
    imprimir(lab_ag)
    dir = ''
    while n < n_P:
        intento += 1
        direccion = rd.randrange(4)
        if direccion == 0 and i > 0:
            dir = 'Arriba'
            i -= 1
        elif direccion == 1 and i < ff - 1:
            dir = 'Abajo'
            i += 1
        elif direccion == 2 and j > 0:
            dir = 'Izquierda'
            j -= 1
        elif direccion == 3 and j < cc - 1:
            dir = 'Derecha'
            j += 1
        else:
            dir = ''
        print("\n Intento " + str(intento))
        if (
            lab_ag[i][j] != muro
            and lab_ag[i][j] != agente
        ):
            if lab_ag[i][j] == pelota:
                print("  Se agarro pelota")
                n += 1
            lab_ag[i_anterior][j_anterior] = espacioRecorrido
            i_anterior = i
            j_anterior = j
            lab_ag[i][j] = agente
        else:
            if dir == 'Arriba':
                i += 1
            elif dir == 'Abajo':
                i -= 1
            elif dir == 'Izquierda':
                j += 1
            elif dir == 'Derecha':
                j -= 1
        print("  Dirección: " + dir + " -> " + str(direccion))
        print("    i: "+str(i)+"\n    j: "+str(j))
        imprimir(lab_ag)


print("LABERINTO\n Laboratorio 1 de SIS420")
c = 10  # int(input("Introduzca la cantidad de columnas del laberinto: "))
f = 11  # int(input("Introduzca la cantidad de filas del laberinto: "))
n_Pelota = 2  # int(input("Introduzca la cantidad de pelotas del laberinto: "))
n_Pared = 60  # int(input("Introduzca la cantidad de muros del laberinto: "))
n_Espacio = (c * f) - n_Pared

laberinto_m = generar_Mapa(c, f)
imprimir(laberinto_m)
Agente(laberinto_m, f, c, n_Pelota)
contador = contar_m(laberinto_m)
print("Hay " + str(contador[0]) + " muros.")
print("Hay " + str(contador[1]) + " espacio.")
print("Hay " + str(contador[2]) + " agente.")
print("Hay " + str(contador[3]) + " espacio recorrido.")
print("Hay " + str(contador[4]) + " pelota.")
