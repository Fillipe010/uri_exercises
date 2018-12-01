X = list(map(int, input().split(" ")))

A = X[0]
B = X[1]
C = X[2]

maior = (A + B + abs(A - B)) / 2

maior = (maior + C + abs(maior - C)) / 2

print("{:} eh o maior".format(int(maior)))