clientes = {}
opcion = ''
while opcion != '6':
    opcion = input('Menu de opciones\n(1)Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElija una opcion: ')
    if opcion == '1':
        rut = input('Ingrese rut del cliente: ')
        nombre = input('Ingrese nombre del cliente: ')
        direccion = input('Ingrese la direccion del cliente: ')
        telefono = input('Ingrese el telefono del cliente: ')
        email = input('Ingrese el email del cliente: ')
        vip = input('Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'direccion':direccion, 'telefono':telefono, 'email':email, 'preferente':vip=='S'}
        clientes[rut] = cliente
    if opcion == '2':
        rut = input('Ingrese el rut del cliente: ')
        if rut in clientes:
            del clientes[rut]
        else:
            print('No existe el cliente con el rut', rut)
    if opcion == '3':
        rut = input('Ingrese el rut del cliente: ')
        if rut in clientes:
            print('rut: ',rut)
            for clave, valor in clientes[rut].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el rut', rut)
    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
print(clientes)