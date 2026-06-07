List = [1, 2, 3, 4, 5, 6]
def Reverse_List(n):
    reversed_List = []
    for i in range(len(n)-1,-1,-1):
        reversed_List.append(n[i])
    return reversed_List

Reversed_List = Reverse_List(List)
print(Reversed_List)