X = int(input())
Y = int(input())
soma = 0
if X > Y:
    lista = range(Y+1,X)
else:
    lista = range(X+1,Y)

for a in lista:
    if a%2 != 0:
        soma+=a
print(soma)