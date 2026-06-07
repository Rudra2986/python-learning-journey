def find_max(n):
    largest = n[0]
    for i in range(0,len(n)) :
        if n[i] > largest:
            largest = n[i]
    return largest
n = [5, 99, 2, 44]
LARGEST_NUM = find_max(n)
print(LARGEST_NUM)