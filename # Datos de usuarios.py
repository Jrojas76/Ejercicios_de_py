# Datos de usuarios
usuarios = [
    ("jaravena", "clave01"),
    ("maravena", "clave02"),
    ("chernandez", "clave03")
]

# Prestaciones para el paciente Martín Aravena
prestaciones_martin = [
    ("FARMACO", 781, "UROCULTIVO, RECUENTO Y ESTUDIO DE SENSIB", 1, 43820),
    ("EXAMEN", 420, "HEMOGRAMA Y VHS", 1, 30324),
    ("EXAMEN", 208, "CREATININA (SANGRE)", 1, 11399),
    ("EXAMEN", 574, "ORINA COMPLETA", 1, 12386),
    ("EXAMEN", 645, "PROTEINA C REACTIVA (CUANTITATIVA)", 1, 35871),
    ("EXAMEN", 599, "PERFIL BIOQUIMICO", 1, 34761),
    ("EXAMEN", 272, "ELECTROLITO NA (SANGRE)", 1, 9984),
    ("EXAMEN", 270, "ELECTROLITO K (SANGRE)", 1, 9984),
    ("EXAMEN", 268, "ELECTROLITO CL (SANGRE)", 1, 9984),
    ("CONSULTA", "P002391", "VISITA INTEGRAL ENFERMERA A DOMICILIO", 1, 65484),
    ("CONSULTA", "P002391", "VISITA INTEGRAL ENFERMERA A DOMICILIO", 1, 65484),
    ("CONSULTA", "C000847", "VISITA MEDICA A DOMICILIO", 1, 125162)
]

# Prestaciones para el paciente Claudia Hernandez
prestaciones_claudia = [
    ("FARMACO", "INS0020-01", "MEDIO DE CONTRASTE NO IONICO", 1, 59524),
    ("EXAMEN", 208, "CREATININA (SANGRE)", 1, 1900),
    ("EXAMEN", "0403001-00", "TAC CRANEO ENCEFALICA", 1, 95870),
    ("EXAMEN", "0403013-00", "TAC TORAX. INC. ESTERNON, CLAVICULA, ART", 1, 142260),
    ("EXAMEN", "0403020-00", "TAC ABDOMEN Y PELVIS", 1, 139790),
    ("EXAMEN", 319, "EXTRACCION DE SANGRE VENOSA ADULTO (CADA", 1, 1230),
    ("CONSULTA", "C000278", "ONCOLOGIA", 1, 23410)
]

cuentas_preparadas = False

# Calcular cuenta sin usar def
total_martin = 0
for prestacion in prestaciones_martin:
    tipo = prestacion[0]
    valor_neto = prestacion[4]
    if tipo == "FARMACO":
        total_martin += valor_neto * 0.20
    elif tipo == "EXAMEN":
        total_martin += valor_neto * 0.10
    elif tipo == "CONSULTA":
        total_martin += valor_neto
total_martin *= 1.19

total_claudia = 0
for prestacion in prestaciones_claudia:
    tipo = prestacion[0]
    valor_neto = prestacion[4]
    if tipo == "FARMACO":
        total_claudia += valor_neto * 0.20
    elif tipo == "EXAMEN":
        total_claudia += valor_neto * 0.10
    elif tipo == "CONSULTA":
        total_claudia += valor_neto
total_claudia *= 1.19

cuentas_preparadas = True

# Simulación del programa sin usar def, while, throw, diccionarios, ni break
usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

usuario_valido = False
for user, pwd in usuarios:
    if user == usuario and pwd == contraseña:
        usuario_valido = True

if usuario_valido:
    print("Inicio de sesión exitoso.")
    if usuario == "jaravena":
        print("Preparando cuentas de pacientes...")
        print("Cuentas preparadas con éxito.")
        volver = input("Presione 1 para volver al menú principal o 2 para salir: ")
        if volver == "2":
            print("Cierre de sesión exitoso, adiós.")
    elif usuario in ["maravena", "chernandez"]:
        if not cuentas_preparadas:
            print("Las cuentas aún no están preparadas. Intente más tarde.")
        else:
            cuenta = total_martin if usuario == "maravena" else total_claudia
            print("1. Consultar deuda")
            print("2. Pagar deuda")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                print(f"Su deuda total es: ${cuenta:.2f}")
            elif opcion == "2":
                print(f"Deuda de ${cuenta:.2f} pagada exitosamente.")
                cuenta = 0
            elif opcion == "3":
                print("Cierre de sesión exitoso, adiós.")
else:
    print("Usuario o contraseña incorrectos.")