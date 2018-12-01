N = int(input())
a = 0

for x in range(N):
	f = a + 1 
	s = a + 2
	t = a + 3
	a = a + 4

	print("{} {} {} PUM".format(f, s, t))