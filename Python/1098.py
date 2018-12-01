i = 0
j = 0

while (i <= 2):
	j = 1
	while (j < 4):
		print("I={} J={}".format(round(i,1),round(j+i,1)))
		j += 1
	i += 0.2
	if (i == 1.0):
		i = 1

	c = round(i,1)

	if (c == 2.0):
		i = 2