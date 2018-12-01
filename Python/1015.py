import math

P1 = list(map(float, input().split(" ")))
P2 = list(map(float, input().split(" ")))

X1 = P1[0]
Y1 = P1[1]
X2 = P2[0]
Y2 = P2[1]

dist = math.sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))

print("{:.4f}".format(dist))