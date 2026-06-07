def list_sum(n) :
    sum = 0
    for i in range(0,len(n)):
        sum += n[i]
    return sum

n = [10, 20, 30, 40]
sum = list_sum(n)
print(sum)


def list_sum2(n) :
    total = 0
    for i in n:
        total += i
    return total
total = list_sum2(n)
print(total)