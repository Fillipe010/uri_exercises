O = input()

mat = [[] for i in range(12)]

for i in range(12):
	for j in range(12):
		mat[i].append(float(input()))

somavlr = 0
media = 0
soma = 0
x = 0

if (O == "M"):
	for i in range(12):
		for j in range(12):
			if (j > i):
				somavlr = somavlr + mat[i][j]
				x = x + 1
				media = somavlr / x
	print("{:.1f}".format(media))

if (O == "S"):
	for i in range(12):
		for j in range(12):
			if (j > i):
				soma = soma + mat[i][j]
	print("{:.1f}".format(soma))