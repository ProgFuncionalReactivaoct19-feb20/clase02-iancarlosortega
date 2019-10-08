"""
	Ejemplo 1: uso de funcion lambda
	@iancarlosortega
"""

datos = [10,2,8,7,5,4,3,11,0, 1]

funcion = lambda x: x**3

print(list(map(funcion,datos)))