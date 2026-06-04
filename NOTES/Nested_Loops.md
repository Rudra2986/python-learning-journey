````md
# Nested Loops

## What is Nested Loop?

Loop inside another loop.

---

## Syntax

```python
for i in range(rows):

    for j in range(columns):
        print("*", end=" ")

    print()
````

---

## Star Pattern Example

```python id="jlwm9r"
for i in range(5):

    for j in range(i + 1):
        print("*", end=" ")

    print()
```

---

## Output

```text
*
* *
* * *
* * * *
* * * * *
```

---

## Reverse Pattern

```python id="jlwm3s"
for i in range(5, 0, -1):

    for j in range(i):
        print("*", end=" ")

    print()
```

---

## Output

```text
* * * * *
* * * *
* * *
* *
*
```

---

## Important Notes

* Outer loop controls rows
* Inner loop controls columns/items
* Commonly used in pattern problems

```
```
