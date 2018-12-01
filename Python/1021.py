A = float(input())

# CEDULAS

cem = int(A / 100)

A = A - (cem * 100)

cinq = int(A / 50)

A = A - (cinq * 50)

vinte = int(A / 20)

A = A - (vinte * 20)

dez = int(A / 10)

A = A - (dez * 10)

cinco = int(A / 5)

A = A - (cinco * 5)

dois = int(A / 2)

A = A - (dois * 2)

# MOEDAS

um = int(A / 1)

A = A - um

cinqCents = int(A / 0.50)

A = A - (cinqCents * 0.50)

vinteCinco = int(A / 0.25)

A = A - (vinteCinco * 0.25)

dezCents = int(A / 0.10)

A = A - (dezCents * 0.10)

cincoCents = int(A / 0.05)

A = A - (cincoCents * 0.05)

umCent = A / 0.01

print("NOTAS:")
print("{:} nota(s) de R$ 100.00".format(cem))
print("{:} nota(s) de R$ 50.00".format(cinq))
print("{:} nota(s) de R$ 20.00".format(vinte))
print("{:} nota(s) de R$ 10.00".format(dez))
print("{:} nota(s) de R$ 5.00".format(cinco))
print("{:} nota(s) de R$ 2.00".format(dois))
print("MOEDAS:")
print("{:} moeda(s) de R$ 1.00".format(um))
print("{:} moeda(s) de R$ 0.50".format(cinqCents))
print("{:} moeda(s) de R$ 0.25".format(vinteCinco))
print("{:} moeda(s) de R$ 0.10".format(dezCents))
print("{:} moeda(s) de R$ 0.05".format(cincoCents))
print("{:} moeda(s) de R$ 0.01".format(int(umCent)))