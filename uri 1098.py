lista = []

for x in range(11):
	lista.append(x/5)

for x in lista:
	if x%2==0:
		print("I=%i J=%i"%(x,1+x))
		print("I=%i J=%i"%(x,2+x))
		print("I=%i J=%i"%(x,3+x))
	else:
		print("I=%.1f J=%.1f"%(x,1+x))
		print("I=%.1f J=%.1f"%(x,2+x))
		print("I=%.1f J=%.1f"%(x,3+x))