from random import randint
# es la libreria que te permite eligir numeros aleatoriamente

print("****************")
print("*QUINIELA: EL TREBOL*")

menu = {
    "1": "Quiniela",
    "2": "Quini 6",
    "3": "Comprobar apuesta",
    "4": "Arqueo de caja",
    "5": "Salir"
}
print("-----------------------")
print("Escoja la deseada:")
print("-----------------------")
for opcion, descripcion in menu.items():
        print(f'* {opcion} - {descripcion}', end="\n")

opcion = int(input("Ingrese la opcion deseada: "))
if opcion == 1:
    apuesta_quiniela = int(input("Ingresar la apuesta de 2, 3 o 4 cifras: "))
    #Generar la apuesta donde tiene que ser un numero de 2, 3 o 4 cifras, con la condicion que sino la cumple no sea correcta la apuesta
    if apuesta_quiniela >= 0 and apuesta_quiniela <= 99:
            numero = apuesta_quiniela
            print(numero)
    elif apuesta_quiniela >= 100 and apuesta_quiniela <= 999:
            numero = apuesta_quiniela
            print(numero)
    elif apuesta_quiniela >= 1000 and apuesta_quiniela <= 9999:
            numero = apuesta_quiniela
            print(numero)
    else:
            print("La apuesta es incorrecta")

    Fecha = input("Ingrese la fecha de la apuesta: ")
    Hora = input("Ingrese la hora de la apuesta: ")
    Numero_comprobante = int(input("Ingrese el numero del comprobante: "))
    DNI = input("Ingrese el numero de DNI: ")
    apuesta_quiniela = input("Ingrese la apuesta: ")

    print("\n----TICKET COMPROBANTE-------------")
    print("Nombre de la quiniela: EL TREBOL")
    print("Fecha: ", Fecha)
    print("Hora: ", Hora)
    print("Numero del comprobante: ", Numero_comprobante)
    print("DNI: ", DNI)
    print("La apuesta es: ", apuesta_quiniela)
    print("\n----------------------------------------")

if opcion ==2:
    menu={"1": "Apuesta",
        "2": "Apuesta al azar"}

    print("-----------------------")
    print("Escoja la deseada:")
    print("-----------------------")
    for opcion, descripcion in menu.items():
        print(f'* {opcion} - {descripcion}', end="\n")

    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        apuesta = [] #la lista esta vacia, le asigno la variable apuesta para que se pueda almacenar
        print("Ingrese su apuesta de 6 números entre 00 y 45 inclusive: ")
        for i in range (6):
            apuesta1 = int(input("Ingrese su apuesta: "))
        if 0 <= apuesta1 <= 45:
                apuesta.append(apuesta1)
        else:
                print("El numero debe estar entre 00 y 45")

    Fecha = input("Ingrese la fecha de la apuesta: ")
    Hora = input("Ingrese la hora de la apuesta: ")
    Numero_comprobante = int(input("Ingrese el numero del comprobante: "))
    DNI = input("Ingrese el numero de DNI: ")

    print("\n----TICKET COMPROBANTE-------------")
    print("Nombre de la quiniela: EL TREBOL")
    print("Fecha: ", Fecha)
    print("Hora: ", Hora)
    print("Numero del comprobante: ", Numero_comprobante)
    print("DNI: ", DNI)
    print("La apuesta es: ", apuesta)
    print("\n----------------------------------------")

    if opcion == 2:
        apuesta_azar = [randint(0,45) for _ in range (6)]

        Fecha = input("Ingrese la fecha de la apuesta: ")
        Hora = input("Ingrese la hora de la apuesta: ")
        Numero_comprobante = int(input("Ingrese el numero del comprobante: "))
        DNI = input("Ingrese el numero de DNI: ")

        print("\n----TICKET COMPROBANTE-------------")
        print("Nombre de la quiniela: EL TREBOL")
        print("Fecha: ", Fecha)
        print("Hora: ", Hora)
        print("Numero del comprobante: ", Numero_comprobante)
        print("DNI: ", DNI)
        print("La apuesta es: ", apuesta_azar)
        print("\n----------------------------------------")