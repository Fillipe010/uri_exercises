L = int(input())
T = input()

mat = [[] for i in range(12)]

for i in range(12):
	for j in range(12):
		mat[i].append(float(input()))

soma = 0
media = 0
somavlr = 0

if (T == "S"):
	for i in range(12):
		soma = soma + mat[L][i]
	print("{:.1f}".format(soma))
		

if (T == "M"):
	for i in range(12):
		somavlr = somavlr + mat[L][i]
		media = somavlr / 12
	print("{:.1f}".format(media))