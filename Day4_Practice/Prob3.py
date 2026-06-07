def count_even(n):
    count = 0
    for i in range(0,len(n)) :
        if n[i]%2 == 0 :
            count += 1
    return count

n = [1, 2, 4, 7, 8]
total_even = count_even(n)
print(total_even)