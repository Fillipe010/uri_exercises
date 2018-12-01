N = int(input())

for i in range(N):
    string = input().split(" ")
    s1,s2 = string
    tNovo = ''
    if(len(s1) <= len(s2)):
        for i in range(len(s1)):
            tNovo += s1[i]
            tNovo += s2[i]
        tNovo += s2[len(s1):]
    else:
        for i in range(len(s2)):
            tNovo += s1[i]
            tNovo += s2[i]
        tNovo += s1[len(s2):]
    print(tNovo)