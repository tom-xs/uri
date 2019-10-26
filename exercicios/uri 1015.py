import math

A,B = [float(x)for x in input().split(" ")]
C,D = [float(x)for x in input().split(" ")]

R = math.sqrt(((A - C) ** 2) + ((B - D) ** 2))

print("%.4f"%R)