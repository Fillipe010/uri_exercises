N = int(input())

vet = []

for i in range(N):
	vet.append(input())

for i in range(N):
	tam = len(vet[i])
	tam2 = int((tam / 2))
	a = vet[i]
	
	print(a[tam2-1::-1] + a[:tam2-1:-1])