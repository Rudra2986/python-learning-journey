````md
# Python Concepts

## Mutable vs Immutable

### Mutable

Can change directly.

Examples:
- lists
- dictionaries

```python
numbers = [1, 2]

numbers.append(3)
````

---

### Immutable

Cannot change directly.

Examples:

* strings
* tuples

```python id="jlwm4h"
text = "Python"
```

---

## Indexing Starts From 0

```python id="jlwm8i"
text = "Python"

print(text[0])
```

Output:

```text id="jlwm1j"
P
```

---

## Off-by-One Error

Very common loop mistake.

```python id="jlwm6k"
range(5)
```

Output:

```text id="jlwm3l"
0 1 2 3 4
```

NOT 5.

---

## Accumulator Pattern

Used for totals/counting.

```python id="jlwm9m"
total = 0

for i in range(1, 6):
    total += i
```

---

## Membership Operator

Checks value existence.

```python id="jlwm5n"
if "a" in "apple":
    print("Found")
```

---

## Infinite Loop

```python id="jlwm2o"
while True:
    print("Running")
```

Stop using:

```text id="jlwm7p"
Ctrl + C
```

---

## Local Variable

Created inside function.

```python id="jlwm4q"
def test():

    x = 10
```

---

## Global Variable

Created outside function.

```python id="jlwm8r"
x = 100

def test():
    print(x)
```

---

## Important Beginner Tips

* Read errors carefully
* Practice daily
* Debug slowly
* Focus on logic
* Write code independently

```
```
