N = int(input())

if ((N % 2) == 0):
	N = N + 1
	print(N)
	for x in range(5):
		N = N + 2
		print(N)
else:
	for x in range(6):
		print(N)
		N = N + 2