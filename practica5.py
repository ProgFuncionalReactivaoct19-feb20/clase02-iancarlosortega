"""
	Ejemplo 1: uso de funcion lambda
	@iancarlosortega
"""
# Se importa "math" para el uso de operacion aritmetica raiz

import math

datos = [(10,2), (8,7), (5,4), (3,11), (10,11)]

raiz = lambda x:x[0]
elevar_cuadrado = lambda x:x[1]

funcion = lambda x: (math.sqrt(raiz(x)),elevar_cuadrado(x)**2)

print(list(map(funcion,datos)))