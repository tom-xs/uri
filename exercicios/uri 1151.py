n = int(input())

lista = []
lista.append(0)
lista.append(1)

for x in range(2,n):
	lista.append(lista[x-1]+lista[x-2])

for x in range(n):
	if lista[x] == lista[-1]:
		print("%i" %lista[x])
	else:
		print("%i "%lista[x], end="")
