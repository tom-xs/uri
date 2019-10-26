A,B = [int(x) for x in input().split(" ")]
if A == B:
    print("O JOGO DUROU 24 HORA(S)")
else:
    if A > B:
        print("O JOGO DUROU %u HORA(S)"%((24-A)+B))
    else:
        print("O JOGO DUROU %u HORA(S)"%(B-A))