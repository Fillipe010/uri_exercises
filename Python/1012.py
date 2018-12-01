P = list(map(float, input().split(" ")))
A = P[0]
B = P[1]
C = P[2]

# TRIANGULO
areaTriangulo = (A * C)/2

# CIRCULO
areaCirculo = (C ** 2) * 3.14159

# TRAPEZIO
areaTrapezio = (C * (A + B)) / 2

# QUADRADO
areaQuadrado = B ** 2

# RETANGULO
areaRetangulo = A * B


print("TRIANGULO: {:.3f}".format(areaTriangulo))
print("CIRCULO: {:.3f}".format(areaCirculo))
print("TRAPEZIO: {:.3f}".format(areaTrapezio))
print("QUADRADO: {:.3f}".format(areaQuadrado))
print("RETANGULO: {:.3f}".format(areaRetangulo))