n = int(input("Enter The Number Of Marks : "))
marks = []
for i in range(0,n):
    mark = int(input("Enter marks : "))
    marks.append(mark)
    
def total_marks(marks):
    total = 0
    for i in range(0,n):
        total += marks[i]
    return total

def avg_marks(marks):
    total = 0
    for i in range(0,n):
        total += marks[i]
    avg = (total/n)
    return avg

def Highest_marks(marks) :
    Highest = marks[0]
    for i in range(0,n):
        if marks[i] > Highest :
            Highest = marks[i]
    return Highest

print("TOTAL MARKS : ",total_marks(marks))
print("AVERAGE MARKS : ",avg_marks(marks))
print("HIGHEST MARKS : ",Highest_marks(marks))