str = input()

lista = str.split(" ")

A = int(lista.__getitem__(0))
B = int(lista.__getitem__(1))
C = int(lista.__getitem__(2))

if A > B:
    if A > C:
        print("%i eh o maior"%A)
    else:
        print("%i eh o maior"%C)
else:
    if B > C:
        print("%i eh o maior"%B)
    else:
        print("%i eh o maior"%C)