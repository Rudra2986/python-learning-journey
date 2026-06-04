````md id="0z43du"
# Lists

## What is List?

List stores multiple values in one variable.

```python
numbers = [1, 2, 3]
````

---

## Access Items

```python id="jlwm5a"
numbers[0]
numbers[-1]
```

---

## Loop Through List

```python id="jlwm2b"
for item in numbers:
    print(item)
```

---

## Important List Functions

| Function  | Use             |
| --------- | --------------- |
| append()  | Add item        |
| insert()  | Add at position |
| remove()  | Remove by value |
| pop()     | Remove by index |
| len()     | Count items     |
| sort()    | Sort list       |
| reverse() | Reverse list    |

---

## append()

Adds item at end.

```python id="jlwm8c"
numbers.append(4)
```

---

## insert()

Adds item at specific index.

```python id="jlwm7d"
numbers.insert(1, 100)
```

---

## remove()

Removes by value.

```python id="jlwm9e"
numbers.remove(2)
```

---

## pop()

Removes by index.

```python id="jlwm4f"
numbers.pop(1)
```

---

## sort()

Sorts list.

```python id="jlwm1g"
numbers.sort()
```

---

## reverse()

Reverses list.

```python id="jlwm3h"
numbers.reverse()
```

---

## Count Items

```python id="jlwm6i"
len(numbers)
```

---

## Example

```python id="jlwm0j"
fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)
```

---

## Important Notes

* Lists are mutable
* Lists can store multiple data types
* Indexing starts from 0

```
```
