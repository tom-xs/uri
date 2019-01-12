A = input()
B = input()

listaA = A.split(" ")
listaB = B.split(" ")

AUni = int(listaA.__getitem__(1))
APre = float(listaA.__getitem__(2))

Buni = int(listaB.__getitem__(1))
BPre = float(listaB.__getitem__(2))

Valor = AUni*APre+Buni*BPre

print("VALOR A PAGAR: R$ %.2F"%Valor)
