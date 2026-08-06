n=5

for i in range(n,0,-1):

    s = 65
    for j in range(1,i+1):
        print(chr(s),end="")
        s+=1

    print()