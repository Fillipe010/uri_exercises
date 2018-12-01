N = 0
a = 0
g = 0
d = 0

while (N != 4):

	N = int(input())

	if(N == 1):
		a = a + 1

	if(N == 2):
		g = g + 1

	if (N == 3):
		d = d + 1

print("MUITO OBRIGADO")
print("Alcool: {}".format(a))
print("Gasolina: {}".format(g))
print("Diesel: {}".format(d))