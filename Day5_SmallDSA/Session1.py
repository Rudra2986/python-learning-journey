# PROBLEM 1 : Sum of Odd Numbers
def sum_odd(numbers):
    total = 0
    for i in numbers:
        if i%2 == 0:
            continue
        else :
            total += i
    return total

num = [1, 2, 3, 4, 5, 6, 7]
SUM_OF_ODD_NUM = sum_odd(num)
print(SUM_OF_ODD_NUM)

# PROBLEM 2 : Count Vowels
def count_vowels(name):
    count = 0
    name = name.lower()
    for i in range (0,len(name)):
        if (name[i] == 'a') or (name[i] == 'e') or (name[i] == 'i') or (name[i] == 'o') or (name[i] == 'u'):
            count += 1
    return count

s = "RudraPatel"
NoOfVowels = count_vowels(s)
print(NoOfVowels)