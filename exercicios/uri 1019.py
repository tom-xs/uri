tempo = int(input())

horas = int(tempo/3600)
minutos = int((tempo % 3600)/60)
segundos = int(((tempo % 3600) % 60))

print(str(horas)+":"+str(minutos)+":"+str(segundos))
