N = int(input())

X = list(map(int, input().split()))

menor = X[0]
posicao = 0

for i in range(N):
	if (X[i] < menor):
		menor = X[i]
		posicao = i

print("Menor valor: {}".format(menor))
print("Posicao: {}".format(posicao))