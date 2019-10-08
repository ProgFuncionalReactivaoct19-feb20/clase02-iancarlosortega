"""
	Ejemplo 5: uso de funcion lambda
	@iancarlosortega
"""

cadena_personalizada = lambda x: "%s capital de %s" % (x[0], x[1]) 


print(cadena_personalizada(("CUENCA", "AZUAY")))