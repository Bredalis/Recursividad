
# Busqueda del dato
# Manera Iterativa

lista = [11, 12, 13, 14, 15, 16, 17]

def Busqueda_Iterativa(lista, dato):

	bajo = 0
	alto = len(lista) - 1
	centro = (bajo + alto) // 2

	while bajo <= alto:

		if lista[centro] == dato:
			return centro

		elif lista[centro] < dato:
			bajo = centro + 1

		else:
			alto = centro - 1

		centro = (bajo + alto) // 2

	return -1

# Manera Recursiva

def Busqueda_Recursiva(lista, bajo, alto, dato):

	if bajo > alto:
		return -1

	centro = (bajo + alto) // 2

	if lista[centro] == dato:
		return centro

	elif lista[centro] < dato:
		return Busqueda_Recursiva(lista, centro + 1, alto, dato)

	else:
		return Busqueda_Recursiva(lista, bajo, centro - 1, dato)

for i in range(10, 19):

	print(f"Iterativa: {i} _ {Busqueda_Iterativa(lista, i)}")
	print(f"Recursiva: {i} _ {Busqueda_Recursiva(lista, 0, len(lista) - 1, i)}")