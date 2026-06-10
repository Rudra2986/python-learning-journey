# Problem 1 → Lowest Number
def find_min(numbers) :
    lowest = numbers[0]
    for i in numbers:
        if lowest > i :
            lowest = i

    return lowest

num = [5, 2, 99, 1, 0]
LowestNum = find_min(num)
print(LowestNum)

# Problem 2 → Check Palindrome
def check_palindrome(string):
    string = string.lower()
    check = 0
    for i in range(0,len(string)//2):
        if string[i] == string[len(string)-i-1]:
            check = 1
        else:
            print("Not A Palindrome")
            break
    if check == 1:
        print("A Palindrome")
    return
string = "Rudra"
check_palindrome(string)

# Problem 3 → Merge Two Lists
def merge_list(a,b):
    for i in range(0,len(b)):
        a.append(b[i])
    return a
a = [1, 2, 3]
b = [4, 5]
c = merge_list(a,b)
print(c)

# Problem 4 → Count Positive / Negative Numbers
def posi_nega_counter(number):
    pcounter = 0
    ncounter = 0
    zcounter = 0
    for i in number :
        if i > 0 :
            pcounter += 1
        elif i < 0 :
            ncounter += 1
        else :
            zcounter +=1
    return pcounter, ncounter, zcounter

n = [-2, 5, -7, 8, 0]
p,n,z = posi_nega_counter(n)
print("Number Of Positives : ",p)
print("Number Of Negatives : ",n)
print("Number Of Zeroes : ",z)
