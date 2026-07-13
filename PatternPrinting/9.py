n = 5
for i in range(1,n+1):

    # print spaces
    for j in range(n-i):
        print(" ", end="")

    # print stars
    for k in range(2*i-1):
        print("*", end="")

    print()
for i in range(n,0,-1):

    # print spaces
    for j in range(n-i):
        print(" ", end="")

    # print stars
    for k in range(2*i-1):
        print("*", end="")
        

    print()