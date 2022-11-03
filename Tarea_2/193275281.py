#Definición de funciones
"""Función que realiza el cálculo del tiempo de navegación""" 
def diasRecorridos(A,B,C):
    global dias
    navegado = A - B
    if B >= A:
        return -1
    if A > C:
        dias = dias + 3
        return dias
    if C > navegado:
        dias = 4 + dias
        C = C - navegado
        diasRecorridos(A,B,C)
    return dias

#Validar que se ingrese un numero positivo
def validarInput():
    n = int(input("Ingrese un número entero positivo: "))
    if n > 0: 
        return n
    else:
        print("El numuro debe ser un Entero Positivo")
        validarInput()

# ENTRADA
A = validarInput()
B = validarInput()
C = validarInput()

# PROCESO
dias = 0
diasNavegados = diasRecorridos(A,B,C)
# SALIDA
if diasNavegados != -1:
    print(round(diasNavegados), " días recorridos")
else: 
    print("Con los parámetros ingresados la expedición no logra arribar a la isla Baffin")
