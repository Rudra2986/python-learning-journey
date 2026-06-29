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


students["student1"]["city"] = "surat"
students["student2"]["city"] = "Ahemedabad"

students["student1"]["Age"] = 19
students["student2"]["Age"] = 23


for student in students:
    for keys in students[student]:
        print(keys, ":", students[student][keys])
    print()