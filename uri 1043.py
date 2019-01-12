A,B,C = [float(x)for x in input().split(" ")]

if A+B > C and A+C > B and C+B > A:
    print("Perimetro = %.1f" %(A+B+C))
else:
    area = ((A + B) * C) / 2
    print("Area = %.1f" % area)
