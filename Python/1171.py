N = int(input())

numeros = {}

for i in range(N):
	x = int(input())
	if(x in numeros):
		numeros[x] += 1
	else:
		numeros[x] = 1


keys = numeros.keys()
keys = sorted(keys)

for j in keys:
	print("%d aparece %d vez(es)" %(j,numeros[j]))