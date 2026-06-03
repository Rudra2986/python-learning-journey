inp = int(input("Enter Number Of Rows : "))
j=1
for i in range(0,inp):
    for j in range(0,i+1):
        print("* ",end="")
    print("")


# Method 2 : specific for python
for i in range(1,inp+1):
    print("* "*i)
