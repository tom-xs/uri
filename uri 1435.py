import numpy as np 

n = 6 
metade = n / 2
matriz = np.ones((n,n))

for a in range(n):
	for b in range(n):
		if a == b :
			matriz[a][b] = (a+b)/2


print(matriz)