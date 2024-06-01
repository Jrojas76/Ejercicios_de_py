#Ahorros y gastos

ahorros = 0
cant_gastos_mensuales = 0
ingreso_mensual = 0
gastos_mensuales = 0

ingreso_mensual = int(input('Ponga su ingreso mensual: '))
cant_gastos_mensuales = int(input('Cuantos tipos de gastos tiene: '))

gastos = []

for i in range(cant_gastos_mensuales):
    gastos_mensuales = float(input(f'Ingrese el gasto {i+1}: '))
    gastos.append(gastos_mensuales)

total_gastos = sum(gastos)
ahorros = ingreso_mensual - total_gastos

print(f'El total de gastos es: {total_gastos}')
print(f'La cantidad de ahorro es: {ahorros}')

if ahorros > 0:
    print('Ha ahorrado')
else:
    print('Ha ido a deficit')