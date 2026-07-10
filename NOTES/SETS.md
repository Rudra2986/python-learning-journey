# Sets in Python

## What is a Set?

A **set** is an unordered collection of **unique** elements.

Properties:
- No duplicate values
- Unordered (no fixed position)
- Mutable (can add/remove elements)
- No indexing
- Faster searching than lists

---

## Creating a Set

```python
numbers = {1, 2, 3, 4}
print(numbers)
```

Output:

```
{1, 2, 3, 4}
```

---

## Empty Set

❌ Wrong

```python
empty = {}
```

This creates an empty dictionary.

✅ Correct

```python
empty = set()
```

---

## Duplicate Values

```python
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)
```

Output:

```
{1, 2, 3, 4}
```

Duplicates are automatically removed.

---

## Add an Element

```python
numbers.add(5)
```

---

## Remove an Element

```python
numbers.remove(2)
```

---

## Check if an Element Exists

```python
if 3 in numbers:
    print("Found")
```

---

## Loop Through a Set

```python
for item in numbers:
    print(item)
```

---

## Convert List to Set

```python
nums = [1, 2, 2, 3, 4, 4]

unique = set(nums)

print(unique)
```

Output:

```
{1, 2, 3, 4}
```

---

## Convert Set Back to List

```python
nums = list(unique)
```

---

# Set Operations

Suppose

```python
A = {1,2,3}
B = {3,4,5}
```

## Union

Everything from both sets.

```python
print(A | B)
```

Output

```
{1,2,3,4,5}
```

---

## Intersection

Common elements.

```python
print(A & B)
```

Output

```
{3}
```

---

## Difference

Elements in A but not in B.

```python
print(A - B)
```

Output

```
{1,2}
```

---

## Difference (Reverse)

Elements in B but not in A.

```python
print(B - A)
```

Output

```
{4,5}
```

---

# Things Sets Cannot Do

❌ Duplicate values

```python
{1,1,2,2}
```

becomes

```
{1,2}
```

---

❌ Indexing

```python
numbers[0]
```

Error

```
TypeError
```

---

❌ Slicing

```python
numbers[1:3]
```

Not possible.

---

❌ Ordered Storage

```python
numbers = {10,20,30,40}
```

Output order is **not guaranteed**.

---

# When to Use Sets

Use sets when you need:

- Remove duplicates
- Fast searching
- Membership checking
- Union
- Intersection
- Difference

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| Add | O(1) |
| Remove | O(1) |
| Search (`in`) | O(1) |
| Union | O(n) |
| Intersection | O(n) |

---

# Quick Revision

Create

```python
s = {1,2,3}
```

Empty Set

```python
s = set()
```

Add

```python
s.add(4)
```

Remove

```python
s.remove(2)
```

Search

```python
3 in s
```

Union

```python
A | B
```

Intersection

```python
A & B
```

Difference

```python
A - B
```

List → Set

```python
set(my_list)
```

Set → List

```python
list(my_set)
```