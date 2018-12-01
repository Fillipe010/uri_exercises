x = int(input())
y = int(input())

soma = 0

if (x > y):
	t = x
	x = y
	y = t

	if ((x % 2) != 0):
		x += 2
		while(x < y):
			if (x % 2 != 0):
				soma = soma + x
			x += 1	
	else:
		x += 1
		while (x < y):
			if (x % 2 != 0):
				soma = soma + x
			x += 1

print(soma)