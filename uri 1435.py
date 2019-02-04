import numpy as np 

n=int(input())

if n%2 == 0:
	u = n/2
else:
	u = (n-1)/2

matriz = np.zeros((n,n))

while(True):
	for a in range(n):
		for b in range(n):
			if a == u or b == u or a == n-(u+1) or b == n-(u+1):
				matriz[a][b] = u+1
	u -= 1
	if u == -1:
		break


for a in range(n):
	for b in range(n):
		if b == 0:
			print("  %i"%(matriz[a][b]),end="")
		else:
			print("   %i"%(matriz[a][b]),end="")
	print()