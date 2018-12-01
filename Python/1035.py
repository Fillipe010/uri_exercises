N = list(map(int, input().split(" ")))

A = N[0]
B = N[1]
C = N[2]
D = N[3]

if ((B > C) and (D > A) and ((C + D) > (A + B)) and ((C > 0) and (D > 0)) and ((A%2) == 0)):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")
	