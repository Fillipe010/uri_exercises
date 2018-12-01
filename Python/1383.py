n = input()

mat = [[] for i in range(9)]

for i in range(9):
	for j in range(9):
		mat[i].append(float(input()))

print(mat)