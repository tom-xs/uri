str = input()

lista = str.split(" ")

A = float(lista.__getitem__(0))
B = float(lista.__getitem__(1))
C = float(lista.__getitem__(2))

AreaTriangulo = A*C/2
AreaCirculo = (C**2)*3.14159
AreaTrapezio = ((A+B)*C)/2
AreaQuadrado = B**2
AreaRetangulo = A*B

print("TRIANGULO: %.3f"%AreaTriangulo)
print("CIRCULO: %.3f"%AreaCirculo)
print("TRAPEZIO: %.3f"%AreaTrapezio)
print("QUADRADO: %.3f"%AreaQuadrado)
print("RETANGULO: %.3f"%AreaRetangulo)