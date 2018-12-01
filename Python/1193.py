x = 1

N = int(input())

while(x <= N):
    string = input().split()
    base = string[1]
    num = string[0]
    
    if base == "bin":
       print("Case "+str(x)+":")
       decimal=int(num,2)
       print(decimal,"dec")
       hexdecimal =hex(int(num,2))
       print(hexdecimal[2:],"hex")
       print()
    
    if base == "dec":
        print("Case "+str(x)+":")
        hexdecimal =hex(int(num))
        print(hexdecimal[2:],"hex")
        print(bin(int(num))[2:],"bin")
        print()
    
    if base == "hex":
        print("Case "+str(x)+":")
        binario = bin(int(num, 16))
        print(int(binario[2:],2),"dec")
        print(binario[2:],"bin")
        print()
    
    x = x + 1