from colorama import Fore, Back, Style

nombre = 'Daniel Quispe Taboada'
colegio = 'Mariscal Sucre "B".'
fecha = '17 de noviembre del 2000'
ciudad = 'Sucre'
domicilio = 'Arturo Posnasky #397'
sangre = '0 positivo'
biografia = 'Yo '+nombre+', naci en Sucre el '+fecha+', mis estudios los realice desde el kinder hasta salir bachiller en el colegio ' + \
    colegio+'\nActualmente estoy estudiando la carrera de Ingenieria de Sistemas en el 7mo semestre. \n '


def inicio():
    repetir = False
    print(Fore.RED + Back.WHITE + " PRACTICA 1 \n  Biografia ")
    print(Style.RESET_ALL)
    print(Fore.BLUE + "Nombre: "+nombre)
    print("Colegio: "+colegio)
    print("Fecha de nacimiento: "+fecha)
    while not repetir:
        print(Fore.WHITE + "\n   Menu ")
        print("  ¯¯¯¯¯¯")
        print("    Biografia = 1")
        print("    Mas Datos = 2")
        print("    Cargar de nuevo = 3")
        print("    Salir = 4")
        metodo = False
        while not metodo:
            opcion = input("Opcion: ")
            if opcion == '1':
                bio()
                metodo = True
            elif opcion == '2':
                datos()
                metodo = True
            elif opcion == '3':
                inicio()
                metodo = True
            elif opcion == '4':
                print("Desea salir?\n  Si = 1\n  No = 2")
                opcion2 = input("Opcion: ")
                if opcion2 == '1':
                    print(Fore.RED + "Saliendo . . .")
                    repetir = True
                    metodo = True
                elif opcion2 == '2':
                    repetir = False
                    metodo = True
                else:
                    print("No existe esa opcion")
                    metodo = False
                    repetir = True
            else:
                print("No hay esa opcion. Elija otra")
                metodo = False


def bio():
    print(Fore.YELLOW + "\nBIOGRAFIA\n"+biografia)


def datos():
    print(Fore.GREEN + "\nNombre: "+nombre)
    print("Colegio: "+colegio)
    print("Fecha de nacimiento: "+fecha)
    print("Lugar de nacimiento: "+ciudad)
    print("Donde vivo: "+domicilio)
    print("Tipo de Sangre: "+sangre)


if __name__ == '__main__':
    inicio()
