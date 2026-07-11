# Tuples in Python

## What is a Tuple?

A **tuple** is an ordered collection of elements that **cannot be changed** after creation.

Example:

```python
student = ("Rudra", 20, 95)
```

---

## Important Notes

- **Tuples are immutable** → You cannot add, remove, or change elements.
- **Tuples are ordered** → Elements keep their order.
- **Allows duplicate values** → Duplicate elements are allowed.
- **Supports indexing** → Access elements using indexes.
- **Supports slicing** → You can slice tuples like lists.
- **Can store multiple data types** → Integers, strings, floats, booleans, lists, dictionaries, etc.
- **Faster than lists** for fixed data.

---

## Creating a Tuple

```python
student = ("Rudra", 20, 95)

print(student)
```

---

## Single Element Tuple

❌ Wrong

```python
numbers = (10)
```

This creates an integer.

✅ Correct

```python
numbers = (10,)
```

The comma is required.

---

## Accessing Elements

```python
student = ("Rudra", 20, 95)

print(student[0])
print(student[1])
print(student[2])
```

Output

```
Rudra
20
95
```

---

## Negative Indexing

```python
print(student[-1])
```

Output

```
95
```

---

## Slicing

```python
student = ("Rudra", 20, 95, "CHARUSAT")

print(student[1:3])
```

Output

```
(20, 95)
```

---

## Loop Through a Tuple

```python
student = ("Rudra", 20, 95)

for item in student:
    print(item)
```

---

## Length of a Tuple

```python
print(len(student))
```

---

## Check if an Element Exists

```python
if "Rudra" in student:
    print("Found")
```

---

## Tuple Packing

Putting multiple values into one tuple.

```python
person = ("Rudra", 20, 95)
```

---

## Tuple Unpacking

Extract values from a tuple.

```python
person = ("Rudra", 20, 95)

name, age, marks = person

print(name)
print(age)
print(marks)
```

Output

```
Rudra
20
95
```

---

## Nested Tuple

```python
students = (
    ("Rudra", 95),
    ("Aman", 88)
)

print(students[0])
print(students[1][1])
```

---

## Convert List to Tuple

```python
numbers = [1, 2, 3]

t = tuple(numbers)

print(t)
```

---

## Convert Tuple to List

```python
numbers = (1, 2, 3)

l = list(numbers)

print(l)
```

---

## Things Tuples Can't Do

❌ Change an element

```python
student[0] = "Aman"
```

Error

```
TypeError
```

---

❌ Add an element

```python
student.append(100)
```

Not possible.

---

❌ Remove an element

```python
student.remove(20)
```

Not possible.

---

## When to Use Tuples

Use tuples when:

- Data should not change.
- Returning multiple values from a function.
- Coordinates (x, y)
- RGB colors
- Database records
- Fixed configurations

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Indexing | O(1) |
| Search (`in`) | O(n) |
| Traversal | O(n) |
| Length | O(1) |

---

## Real-Life Example

```python
student = ("Rudra", 20, "CHARUSAT", 95)
```

A student's basic information usually doesn't change frequently, so a tuple is a good choice.

---

## Quick Revision

Create

```python
t = (1, 2, 3)
```

Single Element

```python
t = (10,)
```

Access

```python
t[0]
```

Slice

```python
t[1:3]
```

Loop

```python
for item in t:
```

Length

```python
len(t)
```

Convert List → Tuple

```python
tuple(my_list)
```

Convert Tuple → List

```python
list(my_tuple)
```

Unpack

```python
a, b, c = t
```

---

# Summary

- Ordered
- Immutable
- Allows duplicates
- Supports indexing and slicing
- Faster than lists for fixed data
- Useful for storing data that should not change