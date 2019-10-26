Ca,Ba,Pa = [int (x) for x in input().split(" ")]
Cr,Br,Pr = [int (x) for x in input().split(" ")]

lista = []

if Cr > Ca:
    lista.append(Cr - Ca)
if Br > Ba:
    lista.append(Br - Ba)
if Pr > Pa:
    lista.append(Pr - Pa)

soma = sum(lista)

print(soma)
