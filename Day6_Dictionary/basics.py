# Creating Dictionary
student = {
    "name": "Rudra",
    "age": 20,
    "marks": 95
}

print(student)

# Accessing Values
print(student["name"])
print(student["marks"])

# Adding New Key-Value Pair
student["city"] = "Ahmedabad"
print(student)

# Updating Value
student["marks"] = 99
print(student)

# Looping Through Dictionary
for key in student:
    print(key, ":", student[key])

# Checking If Key Exists
if "name" in student:
    print("Key Exists")

# Removing Key
student.pop("age")
print(student)

# Dictionary Length
print(len(student))

# Nested Dictionary
students = {
    "student1": {
        "name": "Rudra",
        "marks": 95
    },

    "student2": {
        "name": "Aman",
        "marks": 88
    }
}

print(students)