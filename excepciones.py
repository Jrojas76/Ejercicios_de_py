# Exceciones
# Cuando ejecutamos códigos en Python, es común que aparezcan errores debido a sintaxis incorrecta, mala manipulación de datos o procesos que no pueden ser compilados. Para manejar estos errores, los lenguajes de programación incorporan excepciones. Las excepciones permiten manejar una serie de errores y notificar al usuario o programador que algo no está funcionando como se esperaba.

# Una excepción en programación es un evento anormal o inesperado que ocurre durante la ejecución de un programa y afecta el flujo normal de ejecución. Las excepciones permiten manejar errores o condiciones excepcionales de manera controlada, evitando que el programa se detenga abruptamente. Cuando ocurre una excepción, el programa genera un objeto que encapsula la información sobre el error y lo pasa a un "administrador de excepciones" encargado de gestionar el problema.

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Ambos argumentos deben ser números.")
    else:
        print(f"El resultado es: {result}")
    finally:
        print("La operación de división ha finalizado.")

# Pruebas
divide(10, 2)    # Operación válida
divide(10, 0)    # Error por división por cero
divide(10, 'a')  # Error por tipo de datos incorrecto
