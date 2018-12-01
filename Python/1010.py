produto1 = input()
produto2 = input()

produto1 = produto1.split(" ")
produto2 = produto2.split(" ")

vlrP1 = float(produto1[2])
qtdP1 = int(produto1[1])
vlrP2 = float(produto2[2])
qtdP2 = int(produto2[1])

total = (qtdP1 * vlrP1) + (qtdP2 * vlrP2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))