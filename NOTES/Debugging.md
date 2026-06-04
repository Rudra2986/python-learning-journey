````md id="jlwm7t"
# Debugging

## What is Debugging?

Finding and fixing errors in code.

---

## Common Errors

| Error | Meaning |
|---|---|
| SyntaxError | Invalid syntax |
| IndentationError | Wrong spacing |
| NameError | Variable not found |
| TypeError | Wrong data type usage |
| IndexError | Invalid index |

---

## SyntaxError Example

```python
print("Hello"
````

Missing bracket.

---

## IndentationError Example

```python
if True:
print("Hello")
```

Indentation missing.

---

## NameError Example

```python
print(age)
```

Variable not created.

---

## TypeError Example

```python
"10" + 5
```

Cannot add string and integer.

---

## IndexError Example

```python
numbers = [1, 2]

print(numbers[5])
```

Invalid index.

---

## Debugging Tips

* Read error carefully
* Check indentation
* Print variables
* Check loop conditions
* Check indexes
* Solve one error at a time

---

## Useful Debug Print

```python
print(variable)
```

Helps check values during execution.

```
```
