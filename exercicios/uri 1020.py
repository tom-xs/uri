idade = int(input())

anos = int(idade/365)
meses = int((idade%365)/30)
dias = int((idade%365)%30)

print("%i ano(s)"%anos)
print("%i mes(es)"%meses)
print("%i dia(s)"%dias)