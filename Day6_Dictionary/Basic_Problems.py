# Problem 1 → Student Dictionary
Student_Name = input("Enter Student Name : ")
Student_Age = int(input("Enter Student Age : "))
Student_Marks = int(input("Enter Student Marks : "))

Student = {
    "name" : Student_Name,
    "age" : Student_Age,
    "marks" : Student_Marks
}

print(Student)
print(Student.items())
print(Student.keys())
print(Student.values())

# Problem 2 → Word Frequency Counter
string = "banana"
freq={}
for char in string:
    if char in freq:
        freq[char] += 1 
    else:
        freq[char] = 1
print(freq)   

# Problem 3 → Marks Lookup
Student_Marks = {
  "rudra": 95,
  "aman": 88,
  "mayur": 79,
}
name = input("Enter Student Name : ")
name = name.lower()
if name in Student_Marks:
    print(name,"'s  Marks Are : ",Student_Marks[name])
else :
    print("Invalid Input")