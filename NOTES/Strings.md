````md
# Strings

## What is String?

A string is collection of characters.

```python
text = "Python"
````

---

## Indexing

```python
text[0]
text[-1]
```

| Character | Index |
| --------- | ----- |
| P         | 0     |
| y         | 1     |
| t         | 2     |
| h         | 3     |

---

## Slicing

```python
text[0:3]
```

Output:

```python
Pyt
```

---

## Reverse String

```python
text[::-1]
```

---

## Important String Functions

| Function  | Purpose          |
| --------- | ---------------- |
| lower()   | lowercase        |
| upper()   | uppercase        |
| replace() | replace text     |
| find()    | find position    |
| len()     | count characters |

---

## Examples

```python
text.lower()

text.upper()

text.replace("a", "x")

len(text)
```

---

## Check Character in String

```python
if "a" in text:
    print("Found")
```

---

## Loop Through String

```python
for ch in text:
    print(ch)
```

---

## Important Notes

* Strings are immutable
* Cannot change directly
* Indexing starts from 0

```
```
