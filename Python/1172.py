vetor = []

for x in range(10):
	vetor.append(input())

inteiro = list(map(int, vetor))

for x in range(10):
	if (inteiro[x] <= 0):
		inteiro[x] = 1
		
for x in range(10):
	print("X[{}] = {}".format(x, inteiro[x]))