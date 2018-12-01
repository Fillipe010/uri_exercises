N = int(input())

segundos = N % 60
minutosAll = int(N / 60)
minutos = minutosAll % 60
horas = int(minutosAll / 60)


print("{:}:{:}:{:}".format(horas, minutos, segundos))