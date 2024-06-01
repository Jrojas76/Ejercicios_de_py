#Cambio moneda

tipo_moneda = ''
dolar = 0.013
euro = 0.011
yen = 1.49
cant_moneda_local = 0
dinero_tr = 0

cant_moneda_local = int(input('Ingrese la cantidad de dinero en la moneda local: '))
tipo_moneda = input('A que tipo de moneda va a cambiar entre Dolar, Euro y Yen: ')

if tipo_moneda == 'Dolar':
    dinero_tr = cant_moneda_local * dolar
    print(f'Tiene {dinero_tr:.2f} dolares')
elif tipo_moneda == 'Euro':
    dinero_tr = cant_moneda_local * euro
    print(f'Tiene {dinero_tr:.2f} euros')
elif tipo_moneda == 'Yen':
    dinero_tr = cant_moneda_local * yen
    print(f'Tiene {dinero_tr:.2f} yenes')
else:
    print('Porfavor ingrese el nombre de la moneda con mayuscula al principio')