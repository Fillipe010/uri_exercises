i = 0
N = []
while (i < 6):
	N.append(float(input()))
	i = i+1

j = 0
cont = 0

while (j < 6):
	if (N[j] > 0):
		cont = cont + 1
	j = j + 1

print("{:} valores positivos".format(cont))