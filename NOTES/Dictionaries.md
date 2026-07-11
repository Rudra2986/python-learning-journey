# Dictionaries in Python

## What is a Dictionary?

A **dictionary** is a collection of **key-value pairs**.

Example:

```python
student = {
    "name": "Rudra",
    "age": 20,
    "marks": 95
}
```

---

## Important Notes

- **Dictionaries are mutable** → You can add, update, or remove key-value pairs.
- **Keys must be unique** → Duplicate keys are not allowed.
- **Values can be duplicated** → Multiple keys can have the same value.
- **Stores data as key-value pairs** → Each key has one corresponding value.
- **Access values using keys, not indexes** → Dictionaries do not use numeric indexing.
- **Can store multiple data types** → Keys and values can be integers, strings, floats, booleans, lists, tuples, dictionaries, etc.
- **Insertion order is preserved** (Python 3.7+).

---

## Creating a Dictionary

```python
student = {
    "name": "Rudra",
    "age": 20,
    "marks": 95
}

print(student)
```

---

## Accessing Values

```python
print(student["name"])
print(student["age"])
print(student["marks"])
```

Output

```
Rudra
20
95
```

---

## Add a New Key

```python
student["city"] = "Ahmedabad"

print(student)
```

---

## Update a Value

```python
student["marks"] = 99

print(student)
```

---

## Remove a Key

```python
student.pop("age")

print(student)
```

---

## Check if a Key Exists

```python
if "name" in student:
    print("Key Found")
```

---

## Loop Through Keys

```python
for key in student:
    print(key)
```

---

## Loop Through Values

```python
for value in student.values():
    print(value)
```

---

## Loop Through Key-Value Pairs

```python
for key, value in student.items():
    print(key, ":", value)
```

---

## Dictionary Methods

### keys()

Returns all keys.

```python
print(student.keys())
```

---

### values()

Returns all values.

```python
print(student.values())
```

---

### items()

Returns key-value pairs.

```python
print(student.items())
```

---

### pop()

Removes a key.

```python
student.pop("marks")
```

---

## Nested Dictionary

```python
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
```

Access nested values

```python
print(students["student1"]["name"])
print(students["student2"]["marks"])
```

---

## Add Data to Nested Dictionary

```python
students["student1"]["city"] = "Surat"
students["student2"]["city"] = "Ahmedabad"
```

---

## Loop Through Nested Dictionary

```python
for student in students:
    print(student)

    for key in students[student]:
        print(key, ":", students[student][key])

    print()
```

---

## Things Dictionaries Can't Do

❌ Duplicate keys

```python
student = {
    "name": "Rudra",
    "name": "Aman"
}
```

Output

```python
{'name': 'Aman'}
```

The latest value replaces the previous one.

---

❌ Indexing

```python
student[0]
```

Error

```
KeyError
```

---

❌ Slicing

```python
student[0:2]
```

Not possible.

---

## When to Use Dictionaries

Use dictionaries when you need:

- Store related information
- Fast searching using keys
- Frequency counting
- JSON/API data
- Student records
- Contact management
- Configuration/settings

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Search by Key | O(1) |
| Add | O(1) |
| Update | O(1) |
| Remove | O(1) |

---

## Real-Life Example

```python
student = {
    "name": "Rudra",
    "age": 20,
    "college": "CHARUSAT",
    "marks": 95
}
```

Instead of remembering:

```python
student[0]
student[1]
student[2]
```

You simply use:

```python
student["name"]
student["age"]
student["college"]
```

which is much easier to read and understand.

---

## Quick Revision

Create

```python
student = {}
```

Add

```python
student["city"] = "Ahmedabad"
```

Access

```python
student["name"]
```

Update

```python
student["marks"] = 99
```

Remove

```python
student.pop("marks")
```

Check Key

```python
"name" in student
```

Loop Keys

```python
for key in student:
```

Loop Values

```python
for value in student.values():
```

Loop Items

```python
for key, value in student.items():
```

Nested Access

```python
students["student1"]["name"]
```

---

# Summary

- Stores data as **key-value pairs**
- Mutable
- Keys must be unique
- Fast searching using keys
- No indexing or slicing
- Commonly used in APIs, JSON, databases, and AI applications