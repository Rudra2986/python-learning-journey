print("Problem 1 : Simple Function ")
def Sayhello():
    print("Hello World")
Sayhello()
print("")

print("Problem 2 : Addition Function ")
def Sum(a,b):
    print(a+b)
Sum(5,9)
print("")

print("Problem 3 : Even/Odd Function ")
def check_even(n):
    if n == 0 :
        print("ZERO")
    elif n%2 == 0 :
        print("EVEN")
    else :
        print("ODD")
check_even(53)
print("")

print("Problem 4 : Largest Number Function")
def largest(a, b, c):
    if a>b :
        if a>c :
            print(a)
    elif b>c :
        if b>a :
            print(b)
    else :
        print(c)
largest(33,11,9)
print("")

print("Problem 5 : Count Vowels")
text = input("Enter TEXT : ")
newt = text.lower()
def count_vowels(text):
    count = 0
    for i in range(0,len(text)) :
        if (text[i] == 'a') or (text[i] == 'e') or (text[i] == 'i') or (text[i] == 'o') or (text[i] == 'u'):
            count += 1
    print(count)
count_vowels(newt)
