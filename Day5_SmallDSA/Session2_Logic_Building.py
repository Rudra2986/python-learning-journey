# Problem 3 : Second Largest Number
def second_largest(numbers) :
    largest = 0
    second = 0
    for i in numbers :
        if i > largest :
            temp = largest
            largest = i
            second = temp
        elif (i > second) and (i < largest):
            second = i
    return second

numbers = [10, 50, 99, 120]
second_largest = second_largest(numbers)
print(second_largest)


# Problem 4 → Remove Duplicates
def remove_duplicates(numbers):
    new_list = []
    for i in range(0,len(numbers)) :
        if i == 0:
            new_list.append(numbers[i])
        elif numbers[i-1] == numbers[i] :
            continue
        else :
            new_list.append(numbers[i])
    return new_list

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6]
numbers = remove_duplicates(numbers)
print(numbers)


#  Problem 5 → Frequency Counter
def Freq_counter(numbers):
    counter_list = []
    counter = 0
    visited = []
    for i in range(0,len(numbers)):
        if numbers[i] in visited :
            continue
        for j in range(i,len(numbers)):
            if numbers[i] == numbers[j]:
                counter += 1
        counter_list.append((numbers[i],counter))
        visited.append(numbers[i])
        counter = 0
    return counter_list

num = [1, 2, 2, 3, 1]
Freq_counter_list = Freq_counter(num)
print(Freq_counter_list)

