
"""
Funciones Recursivas: son funciones 
que se llaman a sí mismas para resolver 
un problema dividiéndolo en instancias más 
pequeñas del mismo problema.

Funciones Iterativas: son funciones que 
utilizan bucles o ciclos para ejecutar 
un conjunto de instrucciones repetidamente 
hasta que se cumple una condición de salida.

Factorizacion: es el proceso matemático de 
descomponer una expresión o número en factores 
más simples que, al multiplicarse juntos, 
producen el valor original.
"""

# Libreria

from time import perf_counter

# Funciones Recursivas

def Recursiva(numero):
	print("Recursiva:\n")

	if numero == 0:
		print(numero)

	else:
		print(numero)
		Recursiva(numero - 1)

def Factorizacion_Recursiva(numero):
	print("\nFactorizacion Recursiva: \n")

	if numero == 0 or numero == 1:
		return 1

	return numero*Factorizacion_Recursiva(numero - 1)

# Funcion Iterativa

def Factorizacion_Iteractiva(numero):
	print("\nFactorizacion Iteractiva: \n")

	if numero == 0 or numero == 1:
		print(1)

	resultado = 1

	for i in range(2, numero + 1):		
		resultado *= i

	return resultado

inicio = perf_counter()

for i in range(10):
	print(i, Factorizacion_Iteractiva(i), Factorizacion_Recursiva(i))

for i in range(10):
	Recursiva(i)

final = perf_counter()

print("Tiempo:", "%0.4f" % (final - inicio))