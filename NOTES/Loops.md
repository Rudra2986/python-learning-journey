````md
# Loops

## for Loop

Used when repetitions are known.

```python
for i in range(1, 6):
    print(i)
````

---

## while Loop

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

## Infinite Loop

```python
while True:
    print("Running")
```

Stop using:

```text
Ctrl + C
```

---

## break

Stops loop immediately.

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

---

## continue

Skips current iteration.

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

---

## range()

### Syntax

```python
range(start, stop, step)
```

---

## Examples

```python
range(1, 6)

range(0, 10, 2)

range(10, 0, -1)
```

---

## Important Notes

* stop value excluded
* indexing starts from 0

```
```