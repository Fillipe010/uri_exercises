N = int(input())

anos = int(N / 365)

N = N - (anos * 365)

meses = int(N / 30)

N = N - (meses * 30)

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(N))