sw = 1

while sw:
    print('Menu Principal:')
    print('1. Ver mi Saldo')
    print('2. Retirar Dinero')
    print('3. Salir')

    try:
        opcion = int(input('Seleccione una opcion: '))
        if opcion < 1 or opcion > 3:
            raise ValueError

        if opcion == 1:
            print('Tiene un saldo de $500000')
            opcion2 = input('Presione 1 para volver atras o presione 2 para salir: ')
            if opcion2 == '2':
                print('Cierre de sesion exitoso')
                sw = 0

        elif opcion == 2:
            print('Transferencia realizada')
            opcion2 = input('Presione 1 para volver atras o presione 2 para salir: ')
            if opcion2 == '2':
                print('Cierre de sesion exitoso')
                sw = 0

        elif opcion == 3:
            print('Cierre de sesion exitoso, adios')
            sw = 0
    except ValueError:
        print('Error, porfavor ingrese una opcion valida')

print('Operacion finalizada')