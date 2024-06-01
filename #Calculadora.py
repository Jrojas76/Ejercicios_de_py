#Calculadora 

notas = 0.0
cant_notas = 0
promedio = 0.0
suma = 0.0

cant_notas = int(input('Ingrese la cantidad notas que desea promediar: '))

mis_notas = []

for i in range(cant_notas):
    notas = float(input(f'Ingrese la nota {i+1}: '))
    mis_notas.append(notas)

suma = sum(mis_notas)

promedio = suma / cant_notas

print(f'El promedio de notas es :{promedio}')

if promedio >= 3.0:
    print('Has aprobado')
else:
    print('Has reprobado')