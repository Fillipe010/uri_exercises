N = []

X = float(input())

N.append(X)

for x in range(100):
	print("N[{}] = {:.4f}".format(x, N[x]))
	X = X / 2
	N.append(X)