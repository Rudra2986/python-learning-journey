print("Prob 1 : Print Numbers")
for i in range(0,10):
    print(i+1,end=" | ")
print("")
print("")


print("Prob 2 : Even Numbers")
for i in range(1,21):
    if i%2 == 0:
        print(i,end=" | ")
print("")
print("")


print("Prob 3 : Multiplication Table")
for i in range(1,11):
    print(f"5 x {i} = {i*5}")
print("")
print("")


print("Prob 4 : Sum of First 10 Numbers")
sum = 0
for i in range(1,11):
    sum += i
    if i == 10:
        print(f"{i} = ",end="")
    else:
        print(f"{i} + ",end="")
print(sum)
print("")
print("")


print("Prob 5 : Countdown")
i=10
while i>=1:
    print(i)
    i-=1