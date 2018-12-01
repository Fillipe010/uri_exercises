N = int(input())

for i in range(N):
	string = str(input()).split(" ")
	vet = sorted(string, key = len, reverse = True)
	palavra = ""
	for j in range(len(vet)):
		palavra += vet[j] + " "
	print(palavra.strip(" "))