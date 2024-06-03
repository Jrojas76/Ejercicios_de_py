#Calculadora conversiones

cantidad = float(input("Ingrese la cantidad de longitud: "))
unidad_inicio = input("Ingrese la unidad de inicio (metros, pies, pulgadas): ")
unidad_fin = input("Ingrese la unidad de fin (metros, pies, pulgadas): ")

if unidad_inicio == 'metros':
    metros = cantidad
elif unidad_inicio == 'pies':
    metros = cantidad * 0.3048
elif unidad_inicio == 'pulgadas':
    metros = cantidad * 0.0254
else:
    print("Unidad de inicio no valida. Use 'metros', 'pies' o 'pulgadas'")
    metros = None

if metros is not None:
    if unidad_fin == 'metros':
        resultado = metros
    elif unidad_fin == 'pies':
        resultado = metros * 3.28084
    elif unidad_fin == 'pulgadas':
        resultado = metros * 39.3701
    else:
        print("Unidad de fin no valida. Use 'metros', 'pies' o 'pulgadas'.")
        resultado = None
    if resultado is not None:
        print(f"{cantidad} {unidad_inicio} son {resultado} {unidad_fin}")
else:
    print("Conversion no realizada debido a unidad de inicio no valida.")
